"""Capture live client homepages for Work cards."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent.parent / "assets" / "work"
OUT.mkdir(parents=True, exist_ok=True)

JOBS = [
    ("https://stampssteel.com/", "stampssteel-home.png"),
    ("https://stampssteel.com/designer.html", "stampssteel-designer.png"),
    ("https://bottomviewfarmtn.com/", "bottomview-home.png"),
    ("https://spiderforce-star.github.io/Roux-s/preview/", "rouxs-home.png"),
]


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1,
            reduced_motion="reduce",
        )
        page = context.new_page()
        page.add_init_script(
            "window.localStorage && localStorage.setItem('wsv-theme','dark');"
        )
        for url, name in JOBS:
            dest = OUT / name
            print(f"capturing {url} -> {dest}")
            page.goto(url, wait_until="domcontentloaded", timeout=90000)
            try:
                page.wait_for_load_state("networkidle", timeout=20000)
            except Exception:
                pass
            page.wait_for_timeout(2500)
            page.evaluate(
                """() => {
                  document.querySelectorAll('video').forEach(v => {
                    try { v.pause(); v.muted = true; } catch (e) {}
                  });
                }"""
            )
            page.screenshot(path=str(dest), full_page=False)
            print(f"  wrote {dest.stat().st_size} bytes")
        browser.close()


if __name__ == "__main__":
    main()
