"""Render the static, offline-readable Applied Thermodynamics notes."""

import argparse
import hashlib
import html
import json
import re
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parents[1]
COURSE = "Applied Thermodynamics"
COURSE_URL = "https://nptel.ac.in/courses/112106314"
EXTENDED_COURSE_URL = "https://nptel.ac.in/courses/112106419"
PLAYLIST = "https://www.youtube.com/playlist?list=PLbMVogVj5nJRgXRZ0xEoBfWELmSo6JvvZ"
CHAPTER_NAME = re.compile(r"chapter-(\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*")
MATH = re.compile(
    r"(?P<code>^ {0,3}(?P<fence>```+|~~~+)[^\n]*\n[\s\S]*?^ {0,3}(?P=fence)[ \t]*$|(?P<ticks>`+)[^\n]*?(?P=ticks))"
    r"|(?P<display>(?<!\\)\$\$[\s\S]+?(?<!\\)\$\$|\\\[[\s\S]+?\\\])"
    r"|(?P<inline>(?<![\\$])\$(?![\s$])[^\n]+?(?<![\\\s])\$(?![\d$])|\\\([^\n]+?\\\))",
    re.MULTILINE,
)

esc = html.escape


def write_json(filename, payload):
    (ROOT / filename).write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8", newline="\n",
    )


def load_inventory(path):
    if path:
        raw = json.loads(path.read_text(encoding="utf-8-sig"))
    else:
        manifest = ROOT / "source-manifest.json"
        raw = json.loads(manifest.read_text(encoding="utf-8"))["lectures"] if manifest.exists() else []
    inventory = []
    seen = set()
    for number, row in enumerate(raw, start=1):
        video_id = row["id"]
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id) or video_id in seen:
            raise ValueError(f"Invalid or repeated video ID in lecture {number}")
        seen.add(video_id)
        title = (row.get("title") or "").strip()
        available = (
            bool(title)
            and row.get("availability") not in {"private", "unavailable"}
            and title.casefold().strip("[]") not in {"private video", "deleted video"}
        )
        catalog_links = row.get("catalog_links", {})
        catalog_lessons = row.get("catalog_lessons", {
            catalog: {
                "week": catalog_links[catalog]["week"],
                "lesson": catalog_links[catalog]["lesson"],
            }
            for catalog in ("112106314", "112106419") if catalog in catalog_links
        })
        source_title = catalog_links.get("112106314", {}).get("title")
        inventory.append({
            "number": number,
            "id": video_id,
            "title": title if available else source_title or row.get("catalog_title") or "Private video",
            "availability": "public" if available else "unavailable",
            "duration_seconds": row.get("duration_seconds", row.get("duration")) if available else None,
            "url": f"https://www.youtube.com/watch?v={video_id}" if available else None,
            "catalog_lessons": catalog_lessons,
            "catalog_title": None if available else source_title or row.get("catalog_title"),
            "replacement_playlist_index": row.get("replacement_playlist_index"),
            "replaces_playlist_index": row.get("replaces_playlist_index"),
        })
    return inventory


def lecture_numbers(spec):
    numbers = []
    for part in spec.split(","):
        span = re.fullmatch(
            r"(?:lectures?\s+)?(\d+)(?:\s*(?:[-–—]|to)\s*(\d+))?",
            part.strip(), re.IGNORECASE,
        )
        if not span:
            raise ValueError(f"Invalid lecture range: {spec}")
        first = int(span[1])
        last = int(span[2] or first)
        if not 0 < first <= last:
            raise ValueError(f"Invalid lecture span: {spec}")
        numbers.extend(range(first, last + 1))
    if len(numbers) != len(set(numbers)):
        raise ValueError(f"Repeated lecture number: {spec}")
    return numbers


def parse_chapter(path, inventory):
    number = int(CHAPTER_NAME.fullmatch(path.stem)[1])
    raw = path.read_text(encoding="utf-8-sig")
    front = re.match(r"\A---[ \t]*\n(.*?)\n---[ \t]*\n", raw, re.DOTALL)
    if not front:
        raise ValueError(f"Missing front matter in {path.name}")
    metadata = {}
    for entry in front[1].splitlines():
        if not entry.strip() or entry.startswith("#"):
            continue
        key, separator, value = entry.partition(":")
        if not separator or key in metadata:
            raise ValueError(f"Invalid metadata line in {path.name}: {entry}")
        value = value.strip()
        if len(value) > 1 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        metadata[key] = value
    for key in ("title", "lectures", "summary"):
        if not metadata.get(key):
            raise ValueError(f"Missing {key} in {path.name}")
    lectures = lecture_numbers(metadata["lectures"])
    if inventory and max(lectures) > len(inventory):
        raise ValueError(f"{path.name} references lecture {max(lectures)} beyond the source inventory")
    if inventory and any(inventory[n - 1]["availability"] != "public" for n in lectures):
        raise ValueError(f"{path.name} cites an unavailable recording as a lecture source")
    body = raw[front.end():].strip()
    first_heading = re.match(r"\A# ([^\n]+)\n", body)
    if first_heading and first_heading[1].strip() == metadata["title"]:
        body = body[first_heading.end():].lstrip()
    if not body:
        raise ValueError(f"Empty chapter body: {path.name}")
    source = metadata.get("source", "")
    if source and not re.fullmatch(r"https://[^\s]+", source):
        raise ValueError(f"Expected a single HTTPS source URL in {path.name}")
    return {
        "number": number,
        "title": metadata["title"],
        "summary": metadata["summary"],
        "lectures": lectures,
        "lecture_label": metadata["lectures"],
        "source": source,
        "file": f"{path.stem}.html",
        "content": path.relative_to(ROOT).as_posix(),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "body": body,
    }


def markdown_body(body):
    tokens = {}
    prefix = "THERMOREADERLATEXTOKEN"
    if prefix in body:
        raise ValueError(f"Reserved template token found in chapter body: {prefix}")

    def protect(match):
        if match.group("code"):
            return match[0]
        kind = "display" if match.group("display") else "inline"
        token = f"{prefix}{len(tokens):06d}END"
        # The same delimiters work for both supported input spellings.
        inner = match[0][2:-2] if kind == "display" or match[0].startswith("\\") else match[0][1:-1]
        left, right = ("\\[", "\\]") if kind == "display" else ("\\(", "\\)")
        tokens[token] = f'<span class="math-{kind}">{left}{esc(inner)}{right}</span>'
        return token

    renderer = markdown.Markdown(
        extensions=["extra", "sane_lists", "toc"],
        extension_configs={"toc": {"toc_depth": "2-3", "anchorlink": False}},
    )
    output = renderer.convert(MATH.sub(protect, body))
    toc = renderer.toc if renderer.toc_tokens else ""
    output = re.sub(
        r"(<p><strong>(?:Solution|Answer)\.?</strong>.*?)(?=<h[23]\b|\Z)",
        r'<details class="solution"><summary>Show solution</summary>\1</details>',
        output,
        flags=re.DOTALL,
    )
    for token, math_html in tokens.items():
        output = output.replace(token, math_html)
        toc = toc.replace(token, math_html)
    return output, toc


def chapter_list(chapters, current=None):
    items = []
    for chapter in chapters:
        selected = ' aria-current="page"' if chapter["number"] == current else ""
        items.append(
            f'<li><a href="{chapter["file"]}"{selected}>'
            f'<span>{chapter["number"]:02d}</span>{esc(chapter["title"])}</a></li>'
        )
    return "<ol>" + "".join(items) + "</ol>"


def page(title, description, main, chapters, current=None, toc="", math=False):
    full_title = COURSE if title == COURSE else f"{title} · {COURSE}"
    scripts = (
        '<script defer src="assets/math-config.js"></script>\n'
        '<script defer src="assets/vendor/mathjax-tex-svg-full.js"></script>\n'
    ) if math else ""
    contents = (
        '<details class="side-panel" open><summary>Course contents</summary>'
        f'{chapter_list(chapters, current)}</details>'
    ) if chapters else ""
    page_sections = (
        '<details class="side-panel page-sections" open><summary>On this page</summary>'
        f'{toc}</details>'
    ) if toc else ""
    sidebar = (
        f'<aside class="sidebar" aria-label="Reading navigation">{page_sections}{contents}</aside>'
        if toc or contents else ""
    )
    index_current = ' aria-current="page"' if title == COURSE else ""
    sources_current = ' aria-current="page"' if title == "Source map" else ""
    references_current = ' aria-current="page"' if title == "References" else ""
    lab_current = ' aria-current="page"' if title == "Numerical lab" else ""
    return f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <meta name="color-scheme" content="dark light">
  <title>{esc(full_title)}</title>
  <link rel="stylesheet" href="assets/book.css">
  {scripts}<script defer src="assets/book.js"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="index.html">{COURSE}</a>
    <nav aria-label="Course">
      <a href="index.html"{index_current}>Chapters</a>
      <a href="source-map.html"{sources_current}>Source map</a>
      <a href="references.html"{references_current}>References</a>
      <a href="code-lab.html"{lab_current}>Numerical lab</a>
    </nav>
    <div class="controls" hidden>
      <button type="button" id="theme-toggle">Light theme</button>
      <button type="button" id="text-toggle" aria-pressed="false">Larger text</button>
      <button type="button" id="solutions-toggle" hidden>Expand solutions</button>
      <button type="button" id="print-page">Print / PDF</button>
    </div>
  </div>
</header>
<div class="layout{" wide" if not sidebar else ""}">
  {sidebar}
  <main id="main">
    {main}
    <footer>Independent study notes for IIT Madras’s NPTEL course, with lectures by Babu Viswanathan and tutorials including V. Raghavan.</footer>
  </main>
</div>
</body>
</html>
"""


def home(chapters, inventory):
    rows = []
    for chapter in chapters:
        rows.append(
            f'<li data-chapter><span class="chapter-number">{chapter["number"]:02d}</span>'
            f'<div><h3><a href="{chapter["file"]}">{esc(chapter["title"])}</a></h3>'
            f'<p>{esc(chapter["summary"])}</p></div>'
            f'<span class="lecture-label">{lecture_label(chapter)}</span></li>'
        )
    description = "Independent study notes for NPTEL Applied Thermodynamics at IIT Madras."
    search = """
    <div class="search" hidden>
      <label for="course-search">Find a chapter</label>
      <input type="search" id="course-search" autocomplete="off">
      <p class="search-feedback" id="search-feedback" role="status"></p>
    </div>
    """ if chapters else ""
    chapter_total = len(chapters)
    count = f'{chapter_total} {"chapter" if chapter_total == 1 else "chapters"}'
    accessible = sum(row["availability"] == "public" for row in inventory)
    source_count = (
        f' <a href="source-map.html">{accessible} public recordings</a> are indexed.'
        if inventory else ""
    )
    main = f"""
    <header class="opening">
      <p class="eyebrow">NPTEL · IIT Madras</p>
      <h1>{COURSE}</h1>
      <p class="lead">Independent study notes following the IIT Madras lectures by Babu Viswanathan and the accompanying tutorials, including V. Raghavan.</p>
      <p><a href="{COURSE_URL}">Original course</a> · <a href="{EXTENDED_COURSE_URL}">Expanded course</a> · <a href="{PLAYLIST}">Lecture playlist</a></p>
    </header>
    <section aria-labelledby="chapters">
      <h2 id="chapters">Chapters</h2>
      <p class="metadata">{count} in this edition.{source_count}</p>
      {search}
      <ol class="chapter-list">{"".join(rows)}</ol>
    </section>"""
    return page(COURSE, description, main, chapters)


def lecture_label(chapter):
    label = chapter["lecture_label"]
    if label.lower().startswith("lecture"):
        return esc(label)
    singular = len(chapter["lectures"]) == 1
    return ("Lecture " if singular else "Lectures ") + esc(label)


def recordings(chapter, inventory):
    if not inventory:
        source = chapter["source"]
        return f'<p><a href="{esc(source)}">Source recording</a></p>' if source else ""
    links = "".join(
        f'<li><a href="{inventory[n - 1]["url"]}">{n:02d}. {esc(inventory[n - 1]["title"])}</a></li>'
        for n in chapter["lectures"]
    )
    return f'<details class="recordings"><summary>Source recordings</summary><ol>{links}</ol></details>'


def render_chapter(chapter, before, after, chapters, inventory):
    body, toc = markdown_body(chapter["body"])
    nav = []
    for relation, label, adjacent in (("prev", "Previous", before), ("next", "Next", after)):
        if adjacent:
            nav.append(
                f'<a rel="{relation}" href="{adjacent["file"]}"><span>{label}</span>'
                f'{esc(adjacent["title"])}</a>'
            )
    main = f"""
    <article class="chapter">
      <header class="opening">
        <p class="eyebrow">Chapter {chapter["number"]:02d} · {lecture_label(chapter)}</p>
        <h1>{esc(chapter["title"])}</h1>
        <p class="lead">{esc(chapter["summary"])}</p>
        {recordings(chapter, inventory)}
      </header>
      <div class="prose">
        {body}
      </div>
    </article>
    <nav class="chapter-nav" aria-label="Chapter navigation">{"".join(nav)}</nav>"""
    return page(
        chapter["title"], chapter["summary"], main, chapters, chapter["number"], toc,
        math='class="math-' in body,
    )


def source_map(chapters, inventory):
    by_lecture = {}
    for chapter in chapters:
        for number in chapter["lectures"]:
            by_lecture.setdefault(number, []).append(chapter)

    rows = []
    for source in inventory:
        number = source["number"]
        links = ", ".join(
            f'<a href="{chapter["file"]}">Chapter {chapter["number"]:02d}</a>'
            for chapter in by_lecture.get(number, [])
        ) or "—"
        seconds = source["duration_seconds"]
        duration = f"{seconds // 60}:{seconds % 60:02d}" if isinstance(seconds, int) else "—"
        title = esc(source["title"])
        if source["url"]:
            title = f'<a href="{source["url"]}">{title}</a>'
        else:
            title += ' <span class="metadata">(private video)</span>' if source["catalog_title"] else ""
        replacement = source["replacement_playlist_index"]
        if replacement:
            title += f' <a href="#lecture-{replacement:02d}">Public replacement</a>'
        rows.append(
            f'<tr id="lecture-{number:02d}"><th scope="row">{number:02d}</th>'
            f'<td>{title}</td>'
            f'<td class="duration">{duration}</td><td>{links}</td></tr>'
        )
    listing = (
        '<div class="table-wrap"><table><caption>Recordings in playlist order</caption>'
        '<thead><tr><th scope="col">Order</th><th scope="col">Recording</th>'
        '<th scope="col">Time</th><th scope="col">Notes</th></tr></thead>'
        f'<tbody>{"".join(rows)}</tbody></table></div>'
    ) if inventory else ""
    description = "Official NPTEL recordings and related chapters in the Applied Thermodynamics notes."
    replacement = next((row for row in inventory if row["replacement_playlist_index"]), None)
    reconciliation = (
        '<p>The original IIT Madras listing credits Babu Viswanathan. The expanded listing '
        'credits V. Raghavan and combines recorded lectures by Viswanathan with tutorials. '
        'The original listing identifies <a href="#lecture-43">playlist entry 43</a> as '
        'Psychrometry Part 5. That recording is private. The expanded listing uses the '
        '<a href="#lecture-73">public recording at playlist entry 73</a> for the same lesson. '
        'The notes place it before Parts 6 and 7.</p>'
    ) if replacement else ""
    main = f"""
    <header class="opening">
      <p class="eyebrow">{COURSE}</p>
      <h1>Source map</h1>
      <p class="lead">{description}</p>
      <p><a href="{COURSE_URL}">Original NPTEL listing</a> · <a href="{EXTENDED_COURSE_URL}">Expanded NPTEL listing</a> · <a href="{PLAYLIST}">YouTube playlist</a></p>
    </header>
    {reconciliation}
    {listing}
    """
    return page("Source map", description, main, chapters)


def numerical_lab(chapters):
    entries = []
    for chapter in chapters:
        filename = f'code/chapter_{chapter["number"]:02d}.py'
        source = (ROOT / filename).read_text(encoding="utf-8")
        entries.append(
            f'<li><span class="chapter-number">{chapter["number"]:02d}</span><div>'
            f'<h3><a href="{chapter["file"]}">'
            f'{esc(chapter["title"])}</a></h3>'
            f'<p><a href="{filename}" download>Download Python source</a></p>'
            '<details class="recordings"><summary>View code</summary>'
            f'<pre><code>{esc(source)}</code></pre></details>'
            '</div></li>'
        )
    main = """
    <header class="opening">
      <h1>Numerical lab</h1>
      <p class="lead">Run the Python calculations behind the chapters.</p>
      <p>Keep the programs together in the <code>code</code> directory.
      Run an individual file from the project root, for example
      <code>python code/chapter_01.py</code>. Some labs import routines from
      earlier chapters in the same directory.</p>
    </header>
    """ + f'<ol class="chapter-list">{"".join(entries)}</ol>'
    return page("Numerical lab", "Download and run the chapter calculations.", main, chapters)


def references(chapters):
    markdown_source = (ROOT / "spec" / "references.md").read_text(encoding="utf-8")
    _, _, body = markdown_source.partition("\n")
    content, _ = markdown_body(body)
    main = (
        '<header class="opening"><h1>References</h1>'
        '<p class="lead">Official course records and technical sources used in the notes.</p>'
        '</header><div class="prose">' + content + '</div>'
    )
    return page("References", "Course attribution and technical references.", main, chapters)


def build(inventory_path, content_dir):
    inventory = load_inventory(inventory_path)
    paths = sorted(path for path in content_dir.glob("*.md") if CHAPTER_NAME.fullmatch(path.stem))
    if content_dir.resolve() != (ROOT / "content").resolve():
        raise ValueError("Place public chapter Markdown in content/")
    chapters = [parse_chapter(path, inventory) for path in paths]
    numbers = [chapter["number"] for chapter in chapters]
    if not numbers or len(numbers) != len(set(numbers)):
        raise ValueError("At least one uniquely numbered chapter is required")

    rendered = {
        "index.html": home(chapters, inventory),
        "source-map.html": source_map(chapters, inventory),
        "references.html": references(chapters),
        "code-lab.html": numerical_lab(chapters),
    }
    for i, chapter in enumerate(chapters):
        previous = chapters[i - 1] if i else None
        following = chapters[i + 1] if i + 1 < len(chapters) else None
        rendered[chapter["file"]] = render_chapter(chapter, previous, following, chapters, inventory)

    for filename, output in rendered.items():
        output = re.sub(r"(?m)^[ \t]+$", "", output)
        (ROOT / filename).write_text(output, encoding="utf-8", newline="\n")
    write_json("chapter-manifest.json", {
        "course": COURSE,
        "chapter_count": len(chapters),
        "chapters": [{key: value for key, value in chapter.items() if key != "body"} for chapter in chapters],
    })
    write_json("source-manifest.json", {
        "course": COURSE,
        "official_course": COURSE_URL,
        "expanded_course": EXTENDED_COURSE_URL,
        "official_playlist": PLAYLIST,
        "lectures": inventory,
    })
    print(f"Built {len(chapters)} chapters and indexed {len(inventory)} lecture recordings.")


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--lecture-inventory", type=Path, help="Verified ordered JSON lecture inventory")
    options = cli.parse_args()
    build(options.lecture_inventory, ROOT / "content")
