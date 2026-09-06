"""Desktop + mobile verification screenshots and checks."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "qa"
OUT.mkdir(parents=True, exist_ok=True)
BASE = "http://127.0.0.1:4173"
ISSUES = []


def check_page(page, label, expect_video=False, mobile=False):
    page.wait_for_timeout(800)
    overflow = page.evaluate(
        """() => {
          const doc = document.documentElement;
          return { scrollWidth: doc.scrollWidth, clientWidth: doc.clientWidth };
        }"""
    )
    if overflow["scrollWidth"] > overflow["clientWidth"] + 1:
        ISSUES.append(f"{label}: horizontal overflow {overflow}")

    yt = page.locator("iframe[src*='youtube']")
    hero = page.locator(".hero")
    if expect_video:
        if yt.count() and hero.count():
            # youtube inside hero is forbidden
            in_hero = page.evaluate(
                """() => {
                  const h = document.querySelector('.hero');
                  if (!h) return false;
                  return !!h.querySelector('iframe[src*="youtube"]');
                }"""
            )
            if in_hero:
                ISSUES.append(f"{label}: YouTube iframe in hero")
        vid = page.locator("#hero-video")
        if vid.count() == 0:
            ISSUES.append(f"{label}: missing native hero video")
        else:
            tag = vid.evaluate(
                """(v) => ({
                  muted: v.muted,
                  loop: v.loop,
                  playsInline: v.playsInline,
                  autoplay: v.autoplay,
                  hasSource: !!v.querySelector('source[src*="wsv-top-entrance"]')
                })"""
            )
            if not tag["muted"] or not tag["loop"] or not tag["playsInline"] or not tag["hasSource"]:
                ISSUES.append(f"{label}: hero video attrs {tag}")

    if mobile:
        if page.locator(".menu-btn").count() == 0:
            ISSUES.append(f"{label}: missing hamburger")
        play = page.locator('.drawer a[href="play.html"]')
        if play.count() == 0:
            ISSUES.append(f"{label}: Play missing from drawer")
    else:
        play = page.locator('.nav-links a[href="play.html"]')
        if play.count() == 0:
            ISSUES.append(f"{label}: Play missing from desktop nav")

    page.screenshot(path=str(OUT / f"{label}.png"), full_page=False)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)

        desk = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
        d = desk.new_page()
        d.goto(f"{BASE}/index.html", wait_until="networkidle", timeout=30000)
        d.wait_for_timeout(1500)
        check_page(d, "home-desktop", expect_video=True, mobile=False)

        for path, name in [
            ("/work.html", "work-desktop"),
            ("/websites.html", "websites-desktop"),
            ("/play.html", "play-desktop"),
            ("/contact.html", "contact-desktop"),
            ("/ai.html", "ai-desktop"),
            ("/films.html", "films-desktop"),
            ("/about.html", "about-desktop"),
            ("/services.html", "services-desktop"),
            ("/marketing.html", "marketing-desktop"),
        ]:
            d.goto(BASE + path, wait_until="domcontentloaded", timeout=30000)
            d.wait_for_timeout(600)
            check_page(d, name, expect_video=False, mobile=False)

        # package prefill
        d.goto(f"{BASE}/contact.html?package=launch", wait_until="domcontentloaded")
        d.wait_for_timeout(400)
        val = d.locator("#package").input_value()
        if val != "Launch":
            ISSUES.append(f"package prefill got {val!r}")
        fields = ["name", "email", "business", "website_or_socials", "package", "message"]
        for f in fields:
            if d.locator(f"[name='{f}']").count() == 0:
                ISSUES.append(f"missing form field {f}")
        opts = d.locator("#package option").all_text_contents()
        joined = " | ".join(opts)
        for need in ("Heavy Site", "Visual sales", "$1,750", "$1,000"):
            if need not in joined:
                ISSUES.append(f"interest dropdown missing {need!r}")
        if "Promo" in joined or "from $1,000" in joined:
            ISSUES.append(f"stale package option: {joined}")

        desk.close()

        mob = browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2,
            is_mobile=True,
            has_touch=True,
        )
        m = mob.new_page()
        m.goto(f"{BASE}/index.html", wait_until="networkidle", timeout=30000)
        m.wait_for_timeout(1500)
        check_page(m, "home-mobile", expect_video=True, mobile=True)
        m.locator(".menu-btn").click()
        m.wait_for_timeout(400)
        m.screenshot(path=str(OUT / "home-mobile-menu.png"))
        if not m.locator(".drawer.is-open").count():
            ISSUES.append("mobile menu did not open")
        m.locator('.drawer a[href="play.html"]').click()
        m.wait_for_timeout(800)
        check_page(m, "play-mobile", expect_video=False, mobile=True)
        m.goto(f"{BASE}/work.html", wait_until="domcontentloaded")
        m.wait_for_timeout(700)
        check_page(m, "work-mobile", expect_video=False, mobile=True)
        m.goto(f"{BASE}/websites.html", wait_until="domcontentloaded")
        m.wait_for_timeout(700)
        check_page(m, "websites-mobile", expect_video=False, mobile=True)
        mob.close()
        browser.close()

    print("ISSUES", len(ISSUES))
    for i in ISSUES:
        print(" -", i)
    if ISSUES:
        raise SystemExit(1)
    print("OK")


if __name__ == "__main__":
    main()
