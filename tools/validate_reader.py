"""Check public reader navigation, source coverage, and local resource links."""

import argparse
import hashlib
from html.parser import HTMLParser
import json
import re
from urllib.parse import parse_qs, unquote, urlsplit

from build_reader import ROOT


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.links = []
        self.problems = []
        self.headings = 0
        self.feed(path.read_text(encoding="utf-8"))
        self.close()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "h1":
            self.headings += 1
        element_id = values.get("id")
        if element_id:
            if element_id in self.ids:
                self.problems.append(f"duplicate ID {element_id!r}")
            self.ids.add(element_id)
        if tag in {"base", "embed", "iframe", "object"}:
            self.problems.append(f"embedded element <{tag}>")
        if any(key.startswith("on") for key in values):
            self.problems.append("inline event handler")
        if tag == "script" and "src" not in values:
            self.problems.append("inline script")
        if tag == "img" and not values.get("alt"):
            self.problems.append("image without alt text")
        for attr in ("href", "src", "poster"):
            if values.get(attr):
                self.links.append((tag, attr, values[attr], values.get("rel")))

    handle_startendtag = handle_starttag


def read_json(filename):
    return json.loads((ROOT / filename).read_text(encoding="utf-8"))


def validate(full=False):
    manifest = read_json("chapter-manifest.json")
    chapters = manifest["chapters"]
    source = read_json("source-manifest.json")["lectures"]
    chapter_paths = [ROOT / chapter["file"] for chapter in chapters]
    page_paths = [
        ROOT / "index.html", ROOT / "source-map.html", ROOT / "references.html",
        ROOT / "code-lab.html", *chapter_paths,
    ]
    pages = {path: Page(path) for path in page_paths}
    errors = []
    links_checked = 0
    covered = set()
    timestamp_links = 0
    timestamp_recordings = set()
    recordings_by_id = {
        row["id"]: row for row in source if row["availability"] == "public"
    }

    for page in pages.values():
        for issue in page.problems:
            errors.append(f"{page.path.name}: {issue}")
        if page.headings != 1:
            errors.append(f"{page.path.name}: expected one H1, found {page.headings}")
        for tag, attr, url, _ in page.links:
            target = urlsplit(url)
            if target.scheme or target.netloc:
                if tag != "a" or attr != "href" or target.scheme not in {"https", "http", "mailto"}:
                    errors.append(f"{page.path.name}: external dependency {url}")
                host = (target.hostname or "").removeprefix("www.")
                query = parse_qs(target.query)
                if host in {"youtube.com", "youtu.be"} and "t" in query:
                    video_id = query.get("v", [target.path.removeprefix("/")])[0]
                    timestamp = re.fullmatch(r"(\d+)s?", query["t"][0])
                    row = recordings_by_id.get(video_id)
                    if not row or not timestamp or int(timestamp[1]) >= row["duration_seconds"]:
                        errors.append(f"{page.path.name}: invalid recording timestamp {url}")
                    else:
                        timestamp_links += 1
                        timestamp_recordings.add(row["number"])
                continue
            links_checked += 1
            if target.path.startswith("/") or "\\" in target.path:
                errors.append(f"{page.path.name}: link must be relative to the reader: {url}")
                continue
            resolved = (page.path.parent / unquote(target.path)).resolve() if target.path else page.path
            if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                errors.append(f"{page.path.name}: missing or out-of-root target {url}")
            elif resolved.parts[len(ROOT.parts)] in {"work", ".git", "spec", "plan"}:
                errors.append(f"{page.path.name}: reader links to private working files: {url}")
            elif target.fragment and resolved.suffix == ".html":
                target_page = pages.get(resolved) or Page(resolved)
                if unquote(target.fragment) not in target_page.ids:
                    errors.append(f"{page.path.name}: broken fragment {url}")

    if len(chapters) != manifest["chapter_count"]:
        errors.append("chapter count in manifest does not match entries")
    if [chapter["number"] for chapter in chapters] != list(range(1, len(chapters) + 1)):
        errors.append("chapter numbers have gaps or are out of order")
    generated_chapters = set(ROOT.glob("chapter-*.html"))
    if generated_chapters != set(chapter_paths):
        errors.append("generated chapter HTML files and chapter manifest disagree")
    for index, (chapter, path) in enumerate(zip(chapters, chapter_paths)):
        digest = hashlib.sha256((ROOT / chapter["content"]).read_bytes()).hexdigest()
        if digest != chapter["sha256"]:
            errors.append(f"{chapter['file']}: source changed without rebuilding")
        covered.update(chapter["lectures"])
        wanted = {}
        if index > 0:
            wanted["prev"] = chapters[index - 1]["file"]
        if index + 1 < len(chapters):
            wanted["next"] = chapters[index + 1]["file"]
        found = {relation: url for _, _, url, relation in pages[path].links if relation in {"prev", "next"}}
        if found != wanted:
            errors.append(f"{path.name}: incorrect previous/next navigation")

    if source:
        public = {row["number"] for row in source if row["availability"] == "public"}
        expected_anchors = {f"lecture-{row['number']:02d}" for row in source}
        if not expected_anchors.issubset(pages[ROOT / "source-map.html"].ids):
            errors.append("source map does not include every lecture inventory position")
        if covered - public:
            errors.append(f"notes cite unavailable or unknown positions: {sorted(covered - public)}")
        if full and public - covered:
            errors.append(f"public recordings without notes: {sorted(public - covered)}")
        if full and public - timestamp_recordings:
            errors.append(f"public recordings without timestamps: {sorted(public - timestamp_recordings)}")
    elif full:
        errors.append("full validation requires a public source inventory")

    report = {
        "chapter_count": len(chapters),
        "html_pages_checked": len(pages),
        "internal_links_checked": links_checked,
        "source_positions": len(source),
        "source_positions_mapped": len(covered),
        "full_source_coverage_checked": full,
        "timestamp_links_checked": timestamp_links,
        "public_recordings_with_timestamps": len(timestamp_recordings),
        "passed": not errors,
        "errors": errors,
    }
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full", action="store_true", help="Require coverage of every public recording")
    args = parser.parse_args()
    result = validate(args.full)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
