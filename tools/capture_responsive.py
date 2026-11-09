"""Capture authentic before/after responsive evidence for A2.1.
Run from the project root after installing Playwright and Chromium.
"""
from __future__ import annotations
import json
import socket
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "docs" / "baseline-before"
OUT = ROOT / "docs" / "screenshots"
VIEWPORTS = [(360, 800, "mobile-360"), (768, 1024, "tablet-768"), (1280, 900, "desktop-1280")]


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def start_server(directory: Path):
    port = free_port()
    proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"],
        cwd=directory,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(0.7)
    return proc, port


def inspect_page(page, errors: list[str], phase: str, screenshot: str):
    page.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(img => img.loading = 'eager')")
    page.wait_for_function("[...document.images].every(img => img.complete)")
    page.screenshot(path=str(OUT / screenshot), full_page=True)
    data = page.evaluate("""() => {
        const grid = document.querySelector('.project-grid');
        const columns = getComputedStyle(grid).gridTemplateColumns.split(' ').filter(Boolean).length;
        const images = [...document.images].map(img => ({
            src: img.getAttribute('src'), loaded: img.complete && img.naturalWidth > 0,
            hasAlt: img.hasAttribute('alt')
        }));
        const links = [...document.querySelectorAll('.main-nav a')].map(a => ({
            label: a.textContent.trim(), href: a.getAttribute('href'),
            targetExists: !!document.querySelector(a.getAttribute('href'))
        }));
        return {
            viewport: {width: innerWidth, height: innerHeight},
            documentWidth: document.documentElement.scrollWidth,
            bodyWidth: document.body.scrollWidth,
            horizontalOverflow: document.documentElement.scrollWidth > innerWidth,
            projectColumns: columns,
            projectCards: document.querySelectorAll('.project-grid > article').length,
            navLinks: links,
            images,
            formCount: document.querySelectorAll('form').length,
            formLabels: document.querySelectorAll('form label').length
        };
    }""")
    data.update({"phase": phase, "pageErrors": errors, "screenshot": f"docs/screenshots/{screenshot}"})
    return data


def main() -> int:
    if not BASELINE.joinpath("index.html").exists():
        print("Missing docs/baseline-before snapshot. Re-extract the original project baseline.", file=sys.stderr)
        return 2
    OUT.mkdir(parents=True, exist_ok=True)
    before_server, before_port = start_server(BASELINE)
    after_server, after_port = start_server(ROOT)
    results = []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            for width, height, label in VIEWPORTS:
                # Before: exact source snapshot from the originally submitted ZIP.
                page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
                before_errors: list[str] = []
                page.on("pageerror", lambda error: before_errors.append(str(error)))
                page.goto(f"http://127.0.0.1:{before_port}/", wait_until="networkidle")
                results.append(inspect_page(page, before_errors, "before", f"before-{label}.png"))
                page.close()

                # After: repaired project in the root directory.
                page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
                after_errors: list[str] = []
                page.on("pageerror", lambda error: after_errors.append(str(error)))
                page.goto(f"http://127.0.0.1:{after_port}/", wait_until="networkidle")
                results.append(inspect_page(page, after_errors, "after", f"{label}.png"))
                page.close()
            browser.close()
    except Exception as error:
        print(f"Capture failed: {error}", file=sys.stderr)
        print("Install dependencies with: pip install playwright && python -m playwright install chromium", file=sys.stderr)
        return 2
    finally:
        before_server.terminate(); before_server.wait(timeout=5)
        after_server.terminate(); after_server.wait(timeout=5)

    report = OUT / "viewport-results.json"
    report.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))
    print(f"Saved report: {report}")

    after = [item for item in results if item["phase"] == "after"]
    expected = {360: 1, 768: 2, 1280: 3}
    failed = any(
        item["horizontalOverflow"]
        or item["pageErrors"]
        or item["projectColumns"] != expected[item["viewport"]["width"]]
        or any(not link["targetExists"] for link in item["navLinks"])
        or any(not image["loaded"] or not image["hasAlt"] for image in item["images"])
        for item in after
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
