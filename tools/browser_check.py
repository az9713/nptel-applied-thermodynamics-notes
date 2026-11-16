"""Check the generated reader in Chromium using offline file URLs."""

import argparse
import json
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]


def inspect_page(page, filename, width):
    page.goto((ROOT / filename).as_uri(), wait_until="load")
    assert page.locator("main h1").count() == 1, f"{filename}: expected one chapter heading"
    assert page.evaluate("document.documentElement.scrollWidth") <= width, f"{filename}: viewport overflow"
    source_math = page.locator(".math-inline, .math-display").count()
    if source_math:
        page.evaluate("async () => await window.MathJax.startup.promise.then(() => true)")
        errors = page.locator("[data-mml-node=merror], mjx-merror, [data-mjx-error]").all_text_contents()
        assert not errors, f"{filename}: MathJax errors: {errors}"
        unrendered = page.locator(".math-inline:not(:has(mjx-container)), .math-display:not(:has(mjx-container))")
        assert unrendered.count() == 0, f"{filename}: {unrendered.count()} equations did not render"
    return source_math


def check_controls(page, chapter):
    page.goto((ROOT / "index.html").as_uri())
    search = page.get_by_role("searchbox")
    search.fill(chapter["title"])
    page.locator("[data-chapter]:visible h3").get_by_role("link", name=chapter["title"], exact=True).click()
    assert page.locator("main h1").text_content() == chapter["title"]
    assert page.get_by_role("link", name="Previous", exact=False).count() >= 1
    solutions = page.locator("details.solution")
    if solutions.count():
        page.get_by_role("button", name="Expand solutions").click()
        assert page.locator("details.solution:not([open])").count() == 0
        page.get_by_role("button", name="Collapse solutions").click()
        assert page.locator("details.solution[open]").count() == 0

    assert page.locator("html").get_attribute("data-theme") == "dark"
    page.get_by_role("button", name="Light theme").click()
    assert page.locator("html").get_attribute("data-theme") == "light"
    page.get_by_role("button", name="Larger text").click()
    assert page.locator("html").evaluate("node => node.classList.contains('large-text')")

    page.get_by_role("link", name="Source map", exact=True).first.click()
    assert "private video" in page.locator("#lecture-43").inner_text()
    page.locator("#lecture-43").get_by_role("link", name="Public replacement").click()
    assert page.evaluate("location.hash") == "#lecture-73"


def check_browser(channel):
    manifest = json.loads((ROOT / "chapter-manifest.json").read_text(encoding="utf-8"))
    chapters = manifest["chapters"]
    companions = [name for name in ("index.html", "source-map.html", "code-lab.html", "references.html")
                  if (ROOT / name).is_file()]
    samples = [chapters[index] for index in sorted({0, 1, len(chapters) // 2, len(chapters) - 1})
               if index < len(chapters)]
    report = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel=channel, headless=True)
        for width, selected in ((1440, chapters), (390, samples)):
            context = browser.new_context(viewport={"width": width, "height": 900}, offline=True)
            page = context.new_page()
            errors, external = [], []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.on("requestfailed", lambda request: errors.append(f"{request.url}: {request.failure}"))
            page.on("request", lambda request: external.append(request.url) if request.url.startswith(("http:", "https:")) else None)
            filenames = companions + [chapter["file"] for chapter in selected]
            equations = sum(inspect_page(page, filename, width) for filename in filenames)
            if len(chapters) >= 2:
                check_controls(page, chapters[1])
            assert not errors, errors
            assert not external, external
            report.append({
                "width_px": width,
                "pages_checked": len(filenames),
                "equations_checked": equations,
                "offline_file_url": True,
                "reader_controls_checked": len(chapters) >= 2,
                "passed": True,
            })
            context.close()
        browser.close()
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--channel", default="chrome", help="Installed Chromium browser channel")
    check_browser(parser.parse_args().channel)
