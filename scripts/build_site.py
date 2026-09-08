"""Render the static GitHub Pages studio."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://webbspinnervisions.net"

NAV = [
    ("index.html", "Home"),
    ("play.html", "Play"),
    ("work.html", "Work"),
    ("websites.html", "Websites"),
    ("services.html", "Services"),
    ("ai.html", "AI"),
    ("films.html", "Films"),
    ("marketing.html", "Marketing"),
    ("about.html", "About"),
]

SOCIAL = [
    ("https://x.com/Webb__X", "X", '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.9 2H22l-6.8 7.8L23 22h-6.5l-5.1-7.5L5.7 22H2.6l7.3-8.3L1 2h6.7l4.6 6.8L18.9 2zm-1.1 18h1.8L6.3 3.9H4.4L17.8 20z"/></svg>'),
    ("https://www.youtube.com/@WebbSpinnerVideos", "YouTube", '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31.5 31.5 0 0 0 0 12a31.5 31.5 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31.5 31.5 0 0 0 24 12a31.5 31.5 0 0 0-.5-5.8zM9.8 15.6V8.4L15.8 12l-6 3.6z"/></svg>'),
    ("https://www.facebook.com/profile.php?id=61572155061749", "Facebook", '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 9h3V6h-3c-2.2 0-4 1.8-4 4v2H8v3h2v7h3v-7h2.6l.4-3H13v-2c0-.6.4-1 1-1z"/></svg>'),
    ("https://www.instagram.com/webbspinnervisions", "Instagram", '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h10a4 4 0 0 1 4 4v10a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V7a4 4 0 0 1 4-4zm10 2H7a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2zm-5 3.2A3.8 3.8 0 1 1 8.2 12 3.8 3.8 0 0 1 12 8.2zm0 1.6A2.2 2.2 0 1 0 14.2 12 2.2 2.2 0 0 0 12 9.8zM17.4 6.6a1 1 0 1 1-1 1 1 1 0 0 1 1-1z"/></svg>'),
]

FILMS = [
    ("8nsN5ESSrY0", "HERO", "Hero HomePage", "The entrance film. Animated brand energy built to live on a site and on social."),
    ("TqUbd7HyNUo", "COMMERCIAL", "Commercial Brand Video", "High-impact commercial work made to win attention and drive leads."),
    ("YuyJKJcaPGY", "LIFESTYLE", "Lifestyle Brand Video", "Craft and atmosphere that sell the outcome, not just the product."),
    ("lxCcSFwQG7E", "TRANSFORM", "Before & After Showcase", "Transformation film for service businesses and local brands."),
    ("Ga7R0sbnzpc", "HOSPITALITY", "Restaurant Video", "Food, room, and brand energy — built to stop the scroll and fill tables."),
    ("7nM4UF3J6TQ", "CUSTOM", "Custom Vehicle Video", "Cinematic reveal and detail film for custom builds and specialty shops."),
    ("_mEvE69qwjY", "BRAND", "WSV Animation", "Animated logo motion for website heroes and social pins."),
]


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def nav_html(active: str) -> str:
    links = []
    for href, label in NAV:
        cls = ' class="is-active"' if href == active else ""
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    desktop = "\n          ".join(links)
    drawer = "\n        ".join(links)
    return f"""
  <header class="site-header">
    <div class="nav">
      <a class="brand" href="index.html" aria-label="Webb Spinner Visions home">
        <img src="assets/brand/shield-mark.png" width="40" height="40" alt="" decoding="async">
        <span class="brand-text"><strong>WEBB SPINNER</strong><span>Visions</span></span>
      </a>
      <nav class="nav-links" aria-label="Primary">
          {desktop}
          <a class="btn btn-primary nav-cta" href="contact.html">Contact Us</a>
      </nav>
      <button class="menu-btn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="drawer">
        <svg class="icon-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
        <svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg>
      </button>
    </div>
  </header>
  <nav class="drawer" id="drawer" hidden aria-label="Mobile">
        {drawer}
        <a class="btn btn-primary" href="contact.html">Contact Us</a>
  </nav>"""


def footer_html() -> str:
    col1 = "\n          ".join(f'<a href="{h}">{l}</a>' for h, l in NAV[:5])
    col2 = "\n          ".join(f'<a href="{h}">{l}</a>' for h, l in NAV[5:])
    col2 += '\n          <a href="contact.html">Contact</a>'
    socials = "\n          ".join(
        f'<a href="{url}" target="_blank" rel="noopener noreferrer" aria-label="{name}">{svg}</a>'
        for url, name, svg in SOCIAL
    )
    return f"""
  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <a class="footer-brand" href="index.html">
          <img src="assets/brand/shield-mark.png" width="44" height="44" alt="" decoding="async">
          <div>
            <strong>Webb Spinner Visions</strong>
            <p>Nashville studio. Serving nationwide.</p>
          </div>
        </a>
        <div class="socials">
          {socials}
        </div>
      </div>
      <div class="footer-col">
        <h3>Studio</h3>
          {col1}
      </div>
      <div class="footer-col">
        <h3>More</h3>
          {col2}
        <a href="mailto:webbspinnervisions@gmail.com">webbspinnervisions@gmail.com</a>
      </div>
    </div>
    <div class="wrap footer-bottom">
      <p>Websites you own. Built to convert. Hosted by you.</p>
      <p>&copy; <span data-year>2026</span> Webb Spinner Visions. All rights reserved.</p>
    </div>
  </footer>
  <a class="btn btn-primary sticky-contact" href="contact.html">Contact Us</a>"""


def form_html(next_path: str, subject: str) -> str:
    nxt = f"{SITE}/{next_path}?sent=true#contact"
    return f"""
        <form id="contact-form" class="form" action="https://formsubmit.co/webbspinnervisions@gmail.com" method="POST">
          <input type="hidden" name="_subject" value="{esc(subject)}">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_template" value="table">
          <input type="hidden" name="_next" value="{nxt}">
          <input class="honey" type="text" name="_honey" tabindex="-1" autocomplete="off">
          <label>Name
            <input type="text" name="name" required autocomplete="name" placeholder="Your name">
          </label>
          <label>Email
            <input type="email" name="email" required autocomplete="email" placeholder="you@company.com">
          </label>
          <label>Business
            <input type="text" name="business" autocomplete="organization" placeholder="Business name">
          </label>
          <label>Website or socials
            <input type="text" name="website_or_socials" placeholder="Site, Facebook, Instagram, X…">
          </label>
          <label>Package interest
            <select id="package" name="package">
              <option value="">Select interest…</option>
              <option value="Launch">Launch Site — One-page ($700)</option>
              <option value="Grow">Grow Site — 2–3 pages, animated hero ($1,250)</option>
              <option value="Heavy">Heavy Site — 5 pages, custom ($2,000)</option>
              <option value="Visual sales">Visual sales — logo, animation, video, cards</option>
              <option value="Software">Software / App development</option>
              <option value="AI">AI Solutions</option>
              <option value="Not sure">Not sure yet — help me choose</option>
            </select>
          </label>
          <label>Message
            <textarea name="message" required rows="5" placeholder="What needs to close?"></textarea>
          </label>
          <button class="btn btn-primary" type="submit">Send Message</button>
        </form>
        <div id="form-success" class="form-success" role="status">
          <h3>Message sent.</h3>
          <p>We will reply from webbspinnervisions@gmail.com. You own everything we build.</p>
        </div>"""


def packages_html() -> str:
    return """
        <div class="pkg-grid">
          <article class="pkg pkg-featured">
            <span class="badge">Most Popular</span>
            <h3>Launch Site</h3>
            <p class="price">$700 <span>deposit $150</span></p>
            <p>A simple professional one-page. Looks like a real business, not a template farm. Fast. Clean. Converts.</p>
            <ul>
              <li>Hero: professional still or slow-rotating social photos — no animated film at this tier</li>
              <li>One-page layout, up to 12 social photos</li>
              <li>Contact form to your email, social links</li>
              <li>Mobile-responsive</li>
              <li>Self-host on your accounts</li>
              <li>Two revision rounds</li>
            </ul>
            <a class="btn btn-primary" href="contact.html?package=launch" data-package="launch">Select Launch</a>
          </article>
          <article class="pkg">
            <h3>Grow Site</h3>
            <p class="price">$1,250 <span>deposit $300</span></p>
            <p>Moderate launch. 2–3 pages. More room to sell products, services, menus, venues, or a quote path.</p>
            <ul>
              <li>Everything in Launch</li>
              <li>Animated hero from your social photos and logo — also pins on Facebook, Instagram, and X</li>
              <li>2–3 pages, custom scope for how they sell</li>
              <li>Photos pulled from your site and socials</li>
              <li>Self-host on your accounts</li>
              <li>Two revision rounds</li>
            </ul>
            <a class="btn btn-steel" href="contact.html?package=grow" data-package="grow">Select Grow</a>
          </article>
          <article class="pkg">
            <h3>Heavy Site</h3>
            <p class="price">$2,000 <span>deposit $500</span></p>
            <p>Five pages. Heavier custom scope. The full storefront — still hosted on accounts you own.</p>
            <ul>
              <li>Everything in Grow</li>
              <li>Animated hero from social/site photos + logo</li>
              <li>5 pages at this rate</li>
              <li>Custom layout per page — menu, quote, gallery, events, services, about</li>
              <li>Self-host on your accounts</li>
              <li>Two revision rounds</li>
            </ul>
            <a class="btn btn-steel" href="contact.html?package=heavy" data-package="heavy">Select Heavy</a>
          </article>
        </div>"""


DISCOUNT_LINE = (
    "Discounts for Sumner, Robertson, Macon, Wilson, and Trousdale counties. "
    "Also for veteran's, charitable, and positive religious based associations."
)


def marquee_html() -> str:
    return f"""
        <div class="discount-marquee" role="region" aria-label="{DISCOUNT_LINE}">
          <div class="discount-marquee-track">
            <p class="discount-marquee-item">{DISCOUNT_LINE}</p>
            <span class="discount-marquee-sep" aria-hidden="true">·</span>
            <p class="discount-marquee-item" aria-hidden="true">{DISCOUNT_LINE}</p>
            <span class="discount-marquee-sep" aria-hidden="true">·</span>
          </div>
        </div>"""


def ownership_html() -> str:
    return """
        <ul class="own-list">
          <li><strong>You own 100%</strong> of the code, photos we place, and the video we make for you.</li>
          <li>The contact form lands in the <strong>inbox you already use</strong>.</li>
          <li>We set hosting on <strong>your accounts</strong>. We are not a $25–$150/month hostage host.</li>
          <li><strong>Deposits start the work.</strong> We do not begin on a handshake.</li>
        </ul>"""


def visual_sales_html() -> str:
    return """
        <header class="section-head">
          <p class="eyebrow">Visual sales</p>
          <h2>Logo, motion, film, cards. Quoted to the job.</h2>
          <p class="lede">Priced after a short meeting. Often bundled with a site package. Quoted to the job, not a guess from a menu.</p>
        </header>
        <div class="cap-grid">
          <article class="card">
            <h3>Logo design</h3>
            <p>A mark that holds up on a truck door, a site header, and a business card.</p>
          </article>
          <article class="card">
            <h3>Logo animation</h3>
            <p>The motion lockup for site heroes and social pins.</p>
          </article>
          <article class="card">
            <h3>Sales promotion videos</h3>
            <p>Stills to film. Social cuts, 30-second hooks, and longer sales pieces when the job needs them.</p>
          </article>
          <article class="card">
            <h3>Business card development</h3>
            <p>The card should match the site. Same type, same metal, same promise.</p>
          </article>
          <article class="card">
            <h3>Visual sales assistance</h3>
            <p>One-sheets, quote leave-behinds, social stills, presentation decks, before/after boards. The collateral that gets the meeting and helps close it.</p>
          </article>
          <article class="card">
            <h3>Tell us what you sell</h3>
            <p>We quote after we see it. Available with a website or after a meeting.</p>
            <p style="margin-top:0.85rem"><a class="btn btn-primary" href="contact.html?package=visual" data-package="visual">Tell us what you sell</a></p>
          </article>
        </div>"""


def business_dev_html() -> str:
    return """
        <header class="section-head">
          <p class="eyebrow">Business development</p>
          <h2 id="bd-heading">Get found. Look like you belong. Take the next job.</h2>
          <p class="lede">Webb Spinner Visions is not a template mill. We build the storefront and the sales tools around it so an owner can take the call, send the quote, and keep the customer.</p>
        </header>
        <ol class="bd-list">
          <li>
            <h3>Conversion storefront</h3>
            <p>A site that asks for the job — quote, menu, booking, contact — not a brochure that sits there.</p>
          </li>
          <li>
            <h3>Ownership and self-hosting</h3>
            <p>Domain, matching email, hosting on your accounts. You are not renting your name from us.</p>
          </li>
          <li>
            <h3>Visual sales system</h3>
            <p>Photo to film, logo to motion, card to site. One look across the truck, the phone, and the homepage.</p>
          </li>
          <li>
            <h3>Sales path design</h3>
            <p>How a stranger becomes an inquiry. Industrial quote in one day. Farm event calendar. Restaurant menu and hours. We lay out the path the business already uses to close.</p>
          </li>
          <li>
            <h3>Offer packaging</h3>
            <p>Launch / Grow / Heavy so the owner picks a real scope instead of an open-ended redesign.</p>
          </li>
          <li>
            <h3>Practical AI and custom software</h3>
            <p>Intake, assistants, internal tools you host and license yourself. Scoped after discovery. No invented menu prices.</p>
          </li>
          <li>
            <h3>Close-the-sale craft</h3>
            <p>Decades in structural steel estimating, value engineering, and design-build sales. The through-line is the same: the work has to close. Pretty that does not produce a call is wasted money.</p>
          </li>
        </ol>"""


def work_card(url: str, domain: str, img: str, alt: str, kicker: str, title: str, text: str) -> str:
    return f"""
        <a class="work-card" href="{url}" target="_blank" rel="noopener noreferrer">
          <div class="browser">
            <div class="browser-bar"><span class="dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="browser-url">{esc(domain)}</span></div>
            <img src="{img}" alt="{esc(alt)}" width="1440" height="900" loading="lazy" decoding="async">
          </div>
          <div class="work-body">
            <span class="kicker">{esc(kicker)}</span>
            <h3>{esc(title)}</h3>
            <p>{esc(text)}</p>
            <span class="go">Visit live site →</span>
          </div>
        </a>"""


def film_card(vid: str, kicker: str, title: str, text: str) -> str:
    return f"""
        <button class="film-card" type="button" data-youtube="{vid}" data-title="{esc(title)}">
          <span class="film-thumb">
            <img src="https://img.youtube.com/vi/{vid}/hqdefault.jpg" alt="" width="480" height="360" loading="lazy" decoding="async">
            <span class="play-mark" aria-hidden="true"><span><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span></span>
          </span>
          <span class="film-body">
            <span class="kicker">{esc(kicker)}</span>
            <h3>{esc(title)}</h3>
            <p>{esc(text)}</p>
          </span>
        </button>"""


def lightbox_html() -> str:
    return """
  <div id="lightbox" class="lightbox" role="dialog" aria-modal="true" aria-hidden="true" aria-labelledby="lightbox-title">
    <div class="lightbox-panel">
      <div class="lightbox-frame" id="lightbox-frame"></div>
      <div class="lightbox-bar">
        <p id="lightbox-title"></p>
        <div>
          <a id="lightbox-yt" href="#" target="_blank" rel="noopener noreferrer" hidden>YouTube</a>
          <button class="icon-btn" id="lightbox-close" type="button" aria-label="Close">✕</button>
        </div>
      </div>
    </div>
  </div>"""


def page(
    *,
    filename: str,
    title: str,
    description: str,
    active: str,
    body: str,
    extra_head: str = "",
    extra_end: str = "",
    og_image: str = f"{SITE}/assets/brand/shield-mark.png",
    canonical: str | None = None,
) -> None:
    canon = canonical or f"{SITE}/{'' if filename == 'index.html' else filename}"
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>__TITLE__</title>
  <meta name="description" content="__DESC__">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="__CANON__">
  <meta property="og:type" content="website">
  <meta property="og:title" content="__TITLE__">
  <meta property="og:description" content="__DESC__">
  <meta property="og:url" content="__CANON__">
  <meta property="og:image" content="__OG__">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@Webb__X">
  <link rel="icon" href="favicon.ico" sizes="any">
  <link rel="icon" href="assets/brand/favicon-32.png" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Space+Grotesk:wght@500;600;700&amp;display=swap">
  <link rel="stylesheet" href="css/site.css">
  __EXTRA_HEAD__
</head>
<body>
  <a class="skip" href="#main">Skip to main content</a>
  __NAV__
  <main id="main">
    __BODY__
  </main>
  __FOOTER__
  __EXTRA_END__
  <script src="js/site.js" defer></script>
</body>
</html>
"""
    html = (
        html.replace("__TITLE__", esc(title))
        .replace("__DESC__", esc(description))
        .replace("__CANON__", canon)
        .replace("__OG__", og_image)
        .replace("__EXTRA_HEAD__", extra_head)
        .replace("__NAV__", nav_html(active))
        .replace("__BODY__", body)
        .replace("__FOOTER__", footer_html())
        .replace("__EXTRA_END__", extra_end)
    )
    (ROOT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)


def redirect(src: str, dest: str) -> None:
    url = f"{SITE}/{dest}"
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={dest}">
  <link rel="canonical" href="{url}">
  <title>Redirecting…</title>
  <script>location.replace("{dest}");</script>
</head>
<body>
  <p><a href="{dest}">Continue to {dest}</a></p>
</body>
</html>
"""
    (ROOT / src).write_text(html, encoding="utf-8")
    print("redirect", src, "->", dest)


ORG_JSON = """<script type="application/ld+json">
{"@context":"https://schema.org","@graph":[
  {"@type":["Organization","LocalBusiness","ProfessionalService"],
   "@id":"https://webbspinnervisions.net/#business",
   "name":"Webb Spinner Visions",
   "url":"https://webbspinnervisions.net",
   "logo":"https://webbspinnervisions.net/assets/brand/shield-mark.png",
   "email":"webbspinnervisions@gmail.com",
   "description":"Nashville studio building websites you own, custom software you host yourself, practical AI, and cinematic brand video. Nationwide.",
   "address":{"@type":"PostalAddress","addressLocality":"Nashville","addressRegion":"TN","addressCountry":"US"},
   "areaServed":{"@type":"Country","name":"United States"},
   "sameAs":["https://x.com/Webb__X","https://www.youtube.com/@WebbSpinnerVideos","https://www.facebook.com/profile.php?id=61572155061749","https://www.instagram.com/webbspinnervisions"],
   "priceRange":"$700–$2000",
   "hasOfferCatalog":{"@type":"OfferCatalog","name":"Website packages","itemListElement":[
     {"@type":"Offer","name":"Launch Site","price":"700.00","priceCurrency":"USD","description":"One-page professional site. Photo or rotating social-photo hero. Deposit $150."},
     {"@type":"Offer","name":"Grow Site","price":"1250.00","priceCurrency":"USD","description":"2–3 pages with animated hero from social photos and logo. Deposit $300."},
     {"@type":"Offer","name":"Heavy Site","price":"2000.00","priceCurrency":"USD","description":"Five pages, custom layout per page, animated hero. Deposit $500."}
   ]}
  }
]}
</script>"""


WORK_CARDS = (
    work_card(
        "https://stampssteel.com",
        "stampssteel.com",
        "assets/work/stampssteel-home.jpg",
        "Stamps Steel Buildings homepage — quality steel frame buildings with quote and 3D designer",
        "Grow / custom · quote path",
        "Stamps Steel Buildings",
        "Pre-engineered metal buildings with a live 3D designer and a clear path to quote.",
    )
    + work_card(
        "https://bottomviewfarmtn.com",
        "bottomviewfarmtn.com",
        "assets/work/bottomview-home.jpg",
        "Bottom View Farm homepage — Portland Tennessee weddings, festivals, and events",
        "Grow / custom · Portland, TN",
        "Bottom View Farm",
        "Weddings, festivals, and a working calendar for a family-owned Tennessee venue.",
    )
    + work_card(
        "https://spiderforce-star.github.io/Roux-s/preview/",
        "Roux's Creole Cafe",
        "assets/work/rouxs-home.jpg",
        "Roux's Creole Cafe homepage — Gallatin restaurant, menu, hours, and food truck",
        "Grow / custom · Gallatin, TN",
        "Roux's Creole Cafe",
        "Menu-first hospitality site — hours, food truck, and a path to order.",
    )
)


def home() -> None:
    films = "".join(film_card(*f) for f in FILMS[:3])
    body = f"""
    <section class="hero" aria-labelledby="hero-heading">
      <div class="hero-media">
        <img class="hero-poster" src="assets/hero-poster.jpg" alt="" width="1104" height="816" decoding="async" fetchpriority="high">
        <video id="hero-video" autoplay muted loop playsinline webkit-playsinline preload="metadata" poster="assets/hero-poster.jpg" aria-label="Webb Spinner Visions cinematic brand film">
          <source src="videos/wsv-top-entrance.mp4" type="video/mp4">
        </video>
      </div>
      <div class="hero-scrim" aria-hidden="true"></div>
      <button class="mute-btn" id="mute-btn" type="button" aria-label="Unmute film" aria-pressed="true">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3 3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4 9.91 6.09 12 8.18V4z"/></svg>
        </button>
      <div class="hero-copy">
        <p class="eyebrow">Websites · Visual sales · Software · AI</p>
        <h1 id="hero-heading" class="display metal">Websites you own.<br>Built to convert.<br>Hosted by you.</h1>
        <p class="lede">Nashville studio. Nationwide. Launch <strong>$700</strong>. Grow <strong>$1,250</strong>. Heavy <strong>$2,000</strong>. You keep the code, the photos we place, and hosting on your accounts.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="contact.html">Contact Us</a>
          <a class="btn btn-ghost" href="work.html">See live work</a>
        </div>
        <p class="hero-note">The film on this page is studio work. Launch sites start with a professional photo hero from your socials.</p>
      </div>
    </section>

    <section class="section" aria-labelledby="work-heading">
      <div class="wrap">
        <header class="section-head">
          <p class="eyebrow">Live work</p>
          <h2 id="work-heading">Sites in the wild. Not mocks.</h2>
          <p class="lede">Click through. Grow / custom work — industrial, venue, and restaurant — owned by the client. Not the $700 Launch tier.</p>
        </header>
        <div class="work-grid">
          {WORK_CARDS}
        </div>
      </div>
    </section>

    <hr class="hairline wrap">

    <section class="section" id="packages" aria-labelledby="pkg-heading">
      <div class="wrap">
        <header class="section-head">
          <p class="eyebrow">Packages</p>
          <h2 id="pkg-heading">Hard prices. Clear scope.</h2>
          <p class="lede">Launch is a photo hero. Grow and Heavy get the animated hero. Visual sales, software, and AI are quoted after we see the job.</p>
        </header>
        {packages_html()}
        {marquee_html()}
        {ownership_html()}
      </div>
    </section>

    <section class="section" aria-labelledby="cap-heading">
      <div class="wrap">
        <header class="section-head">
          <p class="eyebrow">Capabilities</p>
          <h2 id="cap-heading">The storefront and the sales tools around it.</h2>
        </header>
        <div class="cap-grid cap-grid-4">
          <article class="card">
            <h3>Website builds</h3>
            <p>Launch $700 · Grow $1,250 · Heavy $2,000. One honest scope instead of an open-ended redesign.</p>
          </article>
          <article class="card">
            <h3>Visual sales</h3>
            <p>Logo, motion, film, cards. Priced after a short meeting. Quoted to the job, not a menu guess.</p>
          </article>
          <article class="card">
            <h3>Software &amp; AI</h3>
            <p>Intake, assistants, internal tools you host and license yourself. Scoped after discovery.</p>
          </article>
          <article class="card">
            <h3>You host it</h3>
            <p>Domain, matching email, hosting on your accounts. We are not a $25–$150/month hostage host.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="bd-heading">
      <div class="wrap">
        {business_dev_html()}
      </div>
    </section>

    <section class="section" aria-labelledby="process-heading">
      <div class="wrap">
        <header class="section-head">
          <p class="eyebrow">Process</p>
          <h2 id="process-heading">Five moves. Then you own it.</h2>
        </header>
        <div class="step-grid">
          <article class="step"><div class="step-num">01</div><h3>Contact</h3><p>Name, email, business, socials, and what you need to convert.</p></article>
          <article class="step"><div class="step-num">02</div><h3>Package</h3><p>Launch $700, Grow $1,250, or Heavy $2,000. Deposit starts the work.</p></article>
          <article class="step"><div class="step-num">03</div><h3>Build</h3><p>Two revision rounds. Launch: photo hero. Grow and Heavy: animated hero.</p></article>
          <article class="step"><div class="step-num">04</div><h3>Host</h3><p>Domain, email, and hosting on your accounts — not ours.</p></article>
          <article class="step"><div class="step-num">05</div><h3>Own</h3><p>Code, photos we place, and any video we make stay with you.</p></article>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="films-heading">
      <div class="wrap">
        <header class="section-head">
          <p class="eyebrow">Films</p>
          <h2 id="films-heading">Motion when the job needs it.</h2>
          <p class="lede">The film on this site is studio work. Launch starts with a professional photo hero from your socials. Grow and Heavy include an animated hero. Gallery films open here — the homepage hero never uses YouTube.</p>
        </header>
        <div class="film-grid">{films}</div>
        <p class="center" style="margin-top:1.5rem"><a class="btn btn-ghost" href="films.html">Full film gallery</a></p>
      </div>
    </section>

    <section class="section" id="contact" aria-labelledby="contact-heading">
      <div class="wrap-narrow">
        <header class="section-head center">
          <p class="eyebrow">Contact</p>
          <h2 id="contact-heading">One honest path.</h2>
          <p class="lede">Tell us the business. We will tell you the package. Prefer email? <a href="mailto:webbspinnervisions@gmail.com">webbspinnervisions@gmail.com</a></p>
        </header>
        {form_html("index.html", "WSV inquiry — Home")}
      </div>
    </section>
    """
    page(
        filename="index.html",
        title="Webb Spinner Visions | Websites you own. Built to convert.",
        description="Nashville studio. Launch $700, Grow $1,250, Heavy $2,000. Websites you own and host yourself. Visual sales, software, and practical AI. Nationwide.",
        active="index.html",
        body=body,
        extra_head=ORG_JSON,
        extra_end=lightbox_html(),
        og_image=f"{SITE}/assets/hero-poster.jpg",
    )


def play() -> None:
    body = """
    <header class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Play · Origin first</p>
        <h1 class="display metal">Spider-Force 5</h1>
        <p class="lede">Original WSV work, built with a few different AI systems, from a love of two games that never left: Asteroids and Star Wars. Origin, then hangar, then the cockpit. Not a screenshot.</p>
      </div>
    </header>

    <section class="section" aria-labelledby="origin-heading">
      <div class="wrap origin-grid">
        <div class="prose">
          <h2 id="origin-heading">How it was made</h2>
          <p>Spider-Force 5 started as a question: could a studio that ships client sites also ship an original game with AI in the loop — and keep the craft honest?</p>
          <p>We built it with a few different AI systems. Original ships. Original systems. The brief was not “remake a classic.” It was: take the feelings that never left, and make something that is ours.</p>
          <p><strong>Asteroids</strong> never left — thrust, drift, inertia, rocks that split when you hit them. You are flying a mass, not a cursor.</p>
          <p><strong>Star Wars</strong> never left — the cockpit, the trench, the targeting. Pressure in a corridor. Not a license. A memory of how it felt to sit in the seat.</p>
          <p>That is the origin. The hangar is next. Then you fly.</p>
        </div>
        <aside class="card">
          <h3>What this is not</h3>
          <p>Not a remake. Not affiliated with Lucasfilm, Disney, or Atari. Original ships, original world, original WSV work — proof that AI craft can ship playable software, not a slide deck.</p>
          <p style="margin-top:0.8rem"><a class="btn btn-ghost" href="ai.html">AI at the studio</a></p>
        </aside>
      </div>
    </section>

    <section class="section" aria-labelledby="hangar-heading">
      <div class="wrap">
        <header class="section-head">
          <p class="eyebrow">Hangar 5</p>
          <h2 id="hangar-heading">Handshake, then launch.</h2>
          <p class="lede">Short and cinematic. Systems come up. Then the live game loads in this page.</p>
        </header>
        <div class="hangar" id="hangar" style="background-image:url('SpiderVenom.jpg')">
          <div class="hangar-veil" aria-hidden="true"></div>
          <div class="hangar-panel">
            <p class="eyebrow">WSV · Original software</p>
            <h3>Canopy closed. Thrust armed.</h3>
            <ul class="sys-list" id="sys-list">
              <li>Thrust / drift model</li>
              <li>Splitting rock field</li>
              <li>Cockpit targeting</li>
              <li>Trench pressure</li>
            </ul>
            <p id="hangar-status" class="note">Origin complete. Enter the hangar to load the live game.</p>
            <div class="btn-row">
              <button class="btn btn-primary" id="hangar-enter" type="button">Enter hangar</button>
              <a class="btn btn-ghost" href="https://spiderforce-star.github.io/Spider-Force-5/" target="_blank" rel="noopener noreferrer">Open game in a new tab</a>
            </div>
          </div>
        </div>
        <div class="game-frame" id="game-frame">
          <iframe id="sf5" title="Spider-Force 5" data-src="https://spiderforce-star.github.io/Spider-Force-5/" allow="gamepad; fullscreen; autoplay" allowfullscreen></iframe>
        </div>
        <p class="legal">Spider-Force 5 is an original game by Webb Spinner Visions. Inspired by the feel of early arcade — Asteroids (thrust, drift, splitting rocks) and Star Wars (cockpit, trench, targeting). Original ships. Not a remake. Not affiliated with Lucasfilm, Disney, or Atari.</p>
        <p class="note">Desktop: WASD / arrows + space / enter / shift. Mobile: on-screen controls. Esc pauses.</p>
      </div>
    </section>
    """
    page(
        filename="play.html",
        title="Play Spider-Force 5 | Origin, hangar, live game — WSV",
        description="Spider-Force 5 is original Webb Spinner Visions work, built with a few different AI systems. Origin story first, hangar handshake, then the live game. Not affiliated with Lucasfilm, Disney, or Atari.",
        active="play.html",
        body=body,
        og_image=f"{SITE}/SpiderVenom.jpg",
    )


def work() -> None:
    body = f"""
    <header class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Work</p>
        <h1 class="display metal">Live sites. Real owners.</h1>
        <p class="lede">Three products in the wild. Screenshots of the live pages — not gray boxes, not concept art. Click any card.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap">
        <div class="work-grid">{WORK_CARDS}</div>
      </div>
    </section>
    <section class="section">
      <div class="wrap split">
        <div>
          <p class="eyebrow">Stamps Steel · 3D designer</p>
          <h2>Industrial software on a brochure site.</h2>
          <p class="lede">The homepage sells the building. The designer lets a buyer set size, doors, and color, then send it for a quote. That is a close path — not a gallery.</p>
          <p><a class="btn btn-ghost" href="https://stampssteel.com/designer.html" target="_blank" rel="noopener noreferrer">Open the 3D designer</a></p>
        </div>
        <a class="work-card" href="https://stampssteel.com/designer.html" target="_blank" rel="noopener noreferrer">
          <div class="browser">
            <div class="browser-bar"><span class="dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="browser-url">stampssteel.com/designer.html</span></div>
            <img src="assets/work/stampssteel-designer.jpg" alt="Stamps Steel 3D designer page" width="1440" height="900" loading="lazy" decoding="async">
          </div>
          <div class="work-body">
            <span class="kicker">Interactive</span>
            <h3>Build it, then quote it</h3>
            <p>Live configuration sitting next to a written quote path.</p>
            <span class="go">Open designer →</span>
          </div>
        </a>
      </div>
    </section>
    <section class="section">
      <div class="wrap cta-band">
        <p>Need a storefront that works this hard? Launch $700, Grow $1,250, Heavy $2,000 — you own it. These live sites are Grow / custom work, not the $700 Launch tier.</p>
        <a class="btn btn-primary" href="contact.html">Contact Us</a>
      </div>
    </section>
    """
    page(
        filename="work.html",
        title="Work | Live sites by Webb Spinner Visions",
        description="Live client work: Stamps Steel Buildings, Bottom View Farm, and Roux's Creole Cafe. Real screenshots of live pages, not mocks.",
        active="work.html",
        body=body,
        og_image=f"{SITE}/assets/work/stampssteel-home.jpg",
    )


def websites() -> None:
    body = f"""
    <header class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Websites</p>
        <h1 class="display metal">You own it. You host it.</h1>
        <p class="lede">Launch $700 · Grow $1,250 · Heavy $2,000. Photo hero on Launch. Animated hero on Grow and Heavy. We are not a monthly hostage host.</p>
        <div class="btn-row" style="margin-top:1.2rem">
          <a class="btn btn-primary" href="contact.html?package=launch" data-package="launch">Contact Us</a>
          <a class="btn btn-ghost" href="work.html">See live work</a>
        </div>
      </div>
    </header>
    <section class="section" id="packages">
      <div class="wrap">
        {packages_html()}
        {marquee_html()}
        {ownership_html()}
        <div class="not-box">
          <h3>What Launch is not</h3>
          <p>Launch is not an animated hero film. It is not 2–3 pages. It is not a five-page custom storefront. It is a professional one-page with a still or slow-rotating social photos — the standard-profile launch. If you have something to show and need it to close, that is Grow. If you need the full storefront, that is Heavy.</p>
        </div>
      </div>
    </section>
    <section class="section" id="visual">
      <div class="wrap">
        {visual_sales_html()}
      </div>
    </section>
    <section class="section" id="hosting">
      <div class="wrap-narrow">
        <header class="section-head">
          <p class="eyebrow">Self-host</p>
          <h2>Five steps. Your accounts.</h2>
          <p class="lede">Agencies often charge $25–$150+ a month to host a site you already paid to build. Self-host can cost $0–$20 after the domain. Setup is included with every website package.</p>
        </header>
        <ol class="host-steps">
          <li>
            <h3>Purchase your domain</h3>
            <p>Register the business name — typically .com; add .net if you want protection. Many registrars offer first-year deals. Secure close spellings so copycats cannot grab lookalikes.</p>
          </li>
          <li>
            <h3>Set up matching email</h3>
            <p>Customers trust you@yourdomain.com. We guide domain email (or hybrid with Gmail for large attachments). The contact form still delivers to the inbox you use every day.</p>
          </li>
          <li>
            <h3>Host on your own account</h3>
            <p>GitHub Pages, Netlify, Cloudflare Pages, or similar — accounts in your name. Optional paid hosts work if you prefer. You are not renting a locked platform from us.</p>
          </li>
          <li>
            <h3>Share a layout you like</h3>
            <p>Send a site you admire plus your social links. We lay out the path the business already uses to close. Launch: up to 12 social photos on one page. Grow: 2–3 pages. Heavy: 5 custom pages.</p>
          </li>
          <li>
            <h3>Hero that matches the package</h3>
            <p>Launch: a professional still or slow-rotating social photos. Grow and Heavy: an animated hero from your photos and logo — the same motion that pins on Facebook, Instagram, and X.</p>
          </li>
        </ol>
        <div class="card" style="margin-top:1.5rem">
          <h3>What is not included</h3>
          <p>Domain registration (you pay the registrar). Optional paid hosting beyond free tiers. Logo design, logo animation, sales film, and business cards — those are visual sales, quoted after a meeting. Pages beyond the package count without a new scope.</p>
        </div>
      </div>
    </section>
    <section class="section" id="contact">
      <div class="wrap-narrow">
        <header class="section-head center">
          <p class="eyebrow">Contact</p>
          <h2>Pick Launch, Grow, or Heavy.</h2>
        </header>
        {form_html("websites.html", "WSV inquiry — Websites")}
      </div>
    </section>
    """
    page(
        filename="websites.html",
        title="Website Builds | Launch $700 · Grow $1,250 · Heavy $2,000",
        description="Websites you own and host yourself. Launch one-page $700 with a photo hero. Grow $1,250 with animated hero, 2–3 pages. Heavy $2,000, five custom pages. Nashville studio.",
        active="websites.html",
        body=body,
    )


def services() -> None:
    body = f"""
    <header class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Services</p>
        <h1 class="display metal">Storefront. Sales tools. You keep both.</h1>
        <p class="lede">Websites you own. Visual sales that match the site. Software and AI you host yourself. Special rates for veterans, charitable, and faith-based organizations.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap three-grid">
        <article class="card">
          <h3>Website builds</h3>
          <p><strong>$700</strong> Launch · <strong>$1,250</strong> Grow · <strong>$2,000</strong> Heavy. Photo hero on Launch. Animated hero on Grow and Heavy. You own the code.</p>
          <p style="margin-top:0.9rem"><a href="websites.html">Website packages →</a></p>
        </article>
        <article class="card">
          <h3>Software &amp; apps you host</h3>
          <p>Custom tools for your business. You host them and license them for your own use. Scoped after discovery. Contact for cost.</p>
          <p style="margin-top:0.9rem"><a href="contact.html?package=software" data-package="software">Request a software quote →</a></p>
        </article>
        <article class="card">
          <h3>AI solutions</h3>
          <p>Assistants, intake, automation, branded tools. Multi-platform so we can match the job. No vendor lock-in. Contact for cost — never a fake AI menu.</p>
          <p style="margin-top:0.9rem"><a href="ai.html">Explore AI →</a></p>
        </article>
      </div>
    </section>
    <section class="section" id="visual">
      <div class="wrap">
        {visual_sales_html()}
      </div>
    </section>
    <section class="section" id="development">
      <div class="wrap">
        {business_dev_html()}
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <header class="section-head">
          <p class="eyebrow">How we work</p>
          <h2>Clear from first email.</h2>
        </header>
        <div class="step-grid">
          <article class="step"><div class="step-num">01</div><h3>Contact</h3><p>Social links, photos, and the outcome you need.</p></article>
          <article class="step"><div class="step-num">02</div><h3>Recommend</h3><p>Launch, Grow, Heavy, or a discovery quote. Deposit to start.</p></article>
          <article class="step"><div class="step-num">03</div><h3>Build</h3><p>Previews until you approve. Two revision rounds on every website package.</p></article>
          <article class="step"><div class="step-num">04</div><h3>Host</h3><p>Domain and hosting on accounts you control.</p></article>
          <article class="step"><div class="step-num">05</div><h3>Own</h3><p>Code, photos we place, and any video we make stay with you.</p></article>
        </div>
      </div>
    </section>
    <section class="section" id="contact">
      <div class="wrap-narrow">
        <header class="section-head center">
          <p class="eyebrow">Contact</p>
          <h2>Tell us what you sell.</h2>
        </header>
        {form_html("services.html", "WSV inquiry — Services")}
      </div>
    </section>
    """
    page(
        filename="services.html",
        title="Services | Websites, visual sales, software you host — WSV",
        description="Launch $700, Grow $1,250, Heavy $2,000. Visual sales quoted after a meeting. Custom software and practical AI you host yourself. Nashville studio, nationwide.",
        active="services.html",
        body=body,
    )


def ai() -> None:
    body = f"""
    <header class="page-hero">
      <div class="wrap">
        <p class="eyebrow">AI</p>
        <h1 class="display metal">Practical AI. No lock-in.</h1>
        <p class="lede">Assistants, intake, automation, branded tools. Multi-platform — we pick the stack for the job. You host it where we can. Contact for cost. We do not publish fake AI menu prices.</p>
        <div class="btn-row" style="margin-top:1.2rem">
          <a class="btn btn-primary" href="contact.html?package=ai" data-package="ai">Contact Us</a>
          <a class="btn btn-ghost" href="play.html">See Spider-Force 5</a>
        </div>
      </div>
    </header>
    <section class="section">
      <div class="wrap cap-grid">
        <article class="card"><h3>Site assistants</h3><p>Answer FAQs, guide visitors to services, capture leads — trained on your business, not generic chat.</p></article>
        <article class="card"><h3>Smart intake</h3><p>Qualify inquiries, collect the right details, route to the right inbox before you pick up the phone.</p></article>
        <article class="card"><h3>Automation</h3><p>Quote helpers, drafts, summaries, and glue between the tools you already run.</p></article>
        <article class="card"><h3>Branded tools</h3><p>Customer-facing utilities that make the company feel current without renting someone else’s platform.</p></article>
        <article class="card"><h3>You control the stack</h3><p>Where possible, solutions run on accounts you own. Same ownership rule as the websites.</p></article>
        <article class="card"><h3>Multi-platform</h3><p>Different models excel at different jobs. We combine them. We do not lock you to one vendor.</p></article>
      </div>
    </section>
    <section class="section">
      <div class="wrap split">
        <div class="prose">
          <p class="eyebrow">Proof of craft</p>
          <h2>Spider-Force 5 is not a gimmick.</h2>
          <p>It is original software we shipped with a few different AI systems — playable, cockpit-first, built from arcade physics and targeting pressure. If we can take AI from a brief to a game you can fly, we can take it to the assistant on your site.</p>
          <p><a class="btn btn-ghost" href="play.html">Origin, hangar, play →</a></p>
        </div>
        <img class="venom" src="SpiderVenom.jpg" alt="Webb Spinner Visions metallic spider" width="1200" height="800" loading="lazy" decoding="async">
      </div>
    </section>
    <section class="section">
      <div class="wrap-narrow">
        <header class="section-head">
          <h2>How an AI project works</h2>
        </header>
        <ol class="host-steps">
          <li><h3>Contact with the problem</h3><p>Not the tech you think you need. The outcome.</p></li>
          <li><h3>Discovery</h3><p>Goals, data you already have, what “done” looks like.</p></li>
          <li><h3>Quote</h3><p>Fixed or phased after scope is clear. No surprise subscription traps from us.</p></li>
          <li><h3>Build &amp; review</h3><p>Working demos early so you can steer.</p></li>
          <li><h3>Deploy on your side</h3><p>You host and control access when the job allows it.</p></li>
        </ol>
        <div class="card" style="margin-top:1.5rem">
          <h3>What we will not do</h3>
          <p>Promise that AI will run the company overnight. Ship tools that lock you into our servers with no exit. Publish fake menu prices for work that needs discovery.</p>
        </div>
      </div>
    </section>
    <section class="section" id="contact">
      <div class="wrap-narrow">
        <header class="section-head center">
          <p class="eyebrow">Contact</p>
          <h2>Ask for cost. We will scope it.</h2>
        </header>
        {form_html("ai.html", "WSV inquiry — AI")}
      </div>
    </section>
    """
    page(
        filename="ai.html",
        title="AI Solutions | Practical tools, no vendor lock-in — WSV",
        description="Practical AI for small business: site assistants, intake, automation, branded tools. Multi-platform. No vendor lock-in. Contact for cost. Spider-Force 5 as proof of craft.",
        active="ai.html",
        body=body,
        og_image=f"{SITE}/SpiderVenom.jpg",
    )


def films() -> None:
    cards = "".join(film_card(*f) for f in FILMS)
    body = f"""
    <header class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Films</p>
        <h1 class="display metal">Heroes, spots, and motion marks.</h1>
        <p class="lede">The film on this site is studio work. Launch sites start with a professional photo hero from your socials. Grow and Heavy include an animated hero. Click a card to play — the homepage hero never uses YouTube.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap">
        <div class="film-grid">{cards}</div>
        <div class="cta-band">
          <p>More on <a href="https://www.youtube.com/@WebbSpinnerVideos" target="_blank" rel="noopener noreferrer">YouTube</a>. Want motion on a Grow or Heavy site, or a quoted sales film? Tell us what you sell.</p>
          <a class="btn btn-primary" href="contact.html">Contact Us</a>
        </div>
      </div>
    </section>
    """
    page(
        filename="films.html",
        title="Films | Website heroes and brand video — Webb Spinner Visions",
        description="Brand films and motion work from Webb Spinner Visions. Grow and Heavy sites include an animated hero. Launch starts with a professional photo hero. Nashville studio.",
        active="films.html",
        body=body,
        extra_end=lightbox_html(),
    )


def marketing() -> None:
    body = f"""
    <header class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Marketing</p>
        <h1 class="display metal">Video. Site. X. Then they contact you.</h1>
        <p class="lede">A local business gets found when the storefront asks for the job, the look matches across truck and phone, and the same name shows up where buyers already look.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap cap-grid">
        <article class="card"><h3>The site</h3><p>Launch, Grow, or Heavy. Clear offer, real photos, contact form to your email. Hosted on your accounts so you are not paying rent to be found.</p></article>
        <article class="card"><h3>The motion</h3><p>Grow and Heavy include an animated hero from your photos and logo — the same asset that pins on Facebook, Instagram, and X. Launch starts with a professional photo hero.</p></article>
        <article class="card"><h3>The feed</h3><p>X, Facebook, Instagram, YouTube — formats that fit each channel. We do not drown you in a 30-post calendar you will not keep.</p></article>
        <article class="card"><h3>Local presence</h3><p>Service-area language, hours, map, and a path to message. Nearby buyers should not have to hunt.</p></article>
        <article class="card"><h3>Lead path</h3><p>One honest CTA: Contact Us. No fake calendars. Inquiries land in the inbox you already live in.</p></article>
        <article class="card"><h3>Visual sales</h3><p>Logo, film, cards, leave-behinds — quoted after a meeting, often bundled with a site. Not a menu price.</p></article>
      </div>
    </section>
    <section class="section">
      <div class="wrap-narrow prose">
        <h2>Motion when it earns the call</h2>
        <p>Still photos get scrolled past. A logo in motion holds the frame. Pin one strong video and it works while you are on the job. That is why Grow and Heavy include the animated hero — not as décor, as distribution.</p>
        <p>Launch is the standard-profile start: a professional still or slow-rotating social photos. Visual sales — logo animation, 30-second hooks, longer pieces — are quoted after we see what you sell.</p>
        <p>We started in video, moved into websites, and now ship the system: storefront that asks for the job, look that matches across the truck and the phone, social that keeps the name in the room.</p>
      </div>
    </section>
    <section class="section" id="contact">
      <div class="wrap-narrow">
        <header class="section-head center">
          <p class="eyebrow">Contact</p>
          <h2>Bring the socials. We will map the path.</h2>
        </header>
        {form_html("marketing.html", "WSV inquiry — Marketing")}
      </div>
    </section>
    """
    page(
        filename="marketing.html",
        title="Marketing | Video, site, and X for local businesses — WSV",
        description="How Webb Spinner Visions uses a site you own, visual sales, and X to get a local business found and contacted. Launch $700, Grow $1,250, Heavy $2,000.",
        active="marketing.html",
        body=body,
    )


def about() -> None:
    body = f"""
    <header class="page-hero">
      <div class="wrap">
        <p class="eyebrow">About</p>
        <h1 class="display metal">Nashville studio. Nationwide close.</h1>
        <p class="lede">Webb Spinner Visions builds websites you own, software you host yourself, practical AI, and cinematic brand video. The through-line is the work has to close.</p>
      </div>
    </header>
    <section class="section">
      <div class="wrap">
        <img class="banner" src="Metallic Header.jpg" alt="Webb Spinner Visions metallic wordmark" width="1600" height="400" decoding="async">
      </div>
    </section>
    <section class="section">
      <div class="wrap split">
        <div class="prose">
          <p>We started in video. We moved into websites. We now ship the storefront and the sales tools around it — at a fraction of agency cost because we use a few different AI systems and keep the owner in control.</p>
          <p>Launch $700 is a professional one-page with a photo hero. Grow $1,250 and Heavy $2,000 include an animated hero. Owners get the code, the photos we place, any video we make, the domain, and hosting on their accounts. We are not a $25–$150/month hostage host.</p>
          <p>Background that still shows up in the work: decades in structural steel estimating, value engineering, and design-build sales. That is why the craft is about closing, not decorating. Pretty that does not produce a call is wasted money.</p>
          <p>Special rates for veterans, charitable, and faith-based organizations. Deposits start the work.</p>
        </div>
        <div>
          <img class="venom" src="SpiderVenom.jpg" alt="" width="1200" height="800" loading="lazy" decoding="async">
          <div class="stat-row">
            <div class="stat"><b>Nashville</b><span>Studio based in Tennessee</span></div>
            <div class="stat"><b>Nationwide</b><span>We ship wherever you host</span></div>
            <div class="stat"><b>Yours</b><span>Code, film, domain, accounts</span></div>
          </div>
        </div>
      </div>
    </section>
    <section class="section" id="contact">
      <div class="wrap-narrow">
        <header class="section-head center">
          <p class="eyebrow">Contact</p>
          <h2>If it has to close, start here.</h2>
        </header>
        {form_html("about.html", "WSV inquiry — About")}
      </div>
    </section>
    """
    page(
        filename="about.html",
        title="About Webb Spinner Visions | Nashville studio, nationwide",
        description="Nashville studio building websites you own, software you host, practical AI, and brand film. Nationwide. The work has to close.",
        active="about.html",
        body=body,
        og_image=f"{SITE}/Metallic Header.jpg",
    )


def contact() -> None:
    body = f"""
    <header class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Contact</p>
        <h1 class="display metal">Contact Us</h1>
        <p class="lede">One path. No fake calendars. Selecting a package on the site prefills interest. Email: <a href="mailto:webbspinnervisions@gmail.com">webbspinnervisions@gmail.com</a></p>
      </div>
    </header>
    <section class="section" id="contact">
      <div class="wrap-narrow">
        {form_html("contact.html", "WSV inquiry — Contact")}
      </div>
    </section>
    """
    page(
        filename="contact.html",
        title="Contact Us | Webb Spinner Visions",
        description="Contact Webb Spinner Visions about Launch $700, Grow $1,250, Heavy $2,000, visual sales, software, or AI. Nashville studio, nationwide. webbspinnervisions@gmail.com",
        active="contact.html",
        body=body,
    )


def extras() -> None:
    not_found = """
    <header class="page-hero">
      <div class="wrap">
        <p class="eyebrow">404</p>
        <h1 class="display metal">This page is not on the site.</h1>
        <p class="lede">Head home, or go straight to Contact Us.</p>
        <div class="btn-row" style="margin-top:1.2rem">
          <a class="btn btn-primary" href="index.html">Home</a>
          <a class="btn btn-ghost" href="contact.html">Contact Us</a>
        </div>
      </div>
    </header>
    """
    page(
        filename="404.html",
        title="Page not found | Webb Spinner Visions",
        description="That page is not on webbspinnervisions.net.",
        active="index.html",
        body=not_found,
        canonical=f"{SITE}/404.html",
    )

    pages = [
        "",
        "play.html",
        "work.html",
        "websites.html",
        "services.html",
        "ai.html",
        "films.html",
        "marketing.html",
        "about.html",
        "contact.html",
    ]
    urls = "\n".join(
        f"  <url><loc>{SITE}/{p}</loc><changefreq>weekly</changefreq></url>" for p in pages
    )
    (ROOT / "sitemap.xml").write_text(
        f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
""",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n",
        encoding="utf-8",
    )
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print("wrote sitemap, robots, 404, .nojekyll")

    for src, dest in [
        ("website.html", "websites.html"),
        ("ai-solutions.html", "ai.html"),
        ("demos.html", "films.html"),
        ("samples.html", "work.html"),
        ("why-video.html", "films.html"),
    ]:
        redirect(src, dest)


def main() -> None:
    home()
    play()
    work()
    websites()
    services()
    ai()
    films()
    marketing()
    about()
    contact()
    extras()
    (ROOT / "README.md").write_text(
        """# Webb Spinner Visions

Studio site for [webbspinnervisions.net](https://webbspinnervisions.net) — GitHub Pages, `CNAME` preserved.

Static HTML/CSS/JS. Native MP4 homepage hero (no YouTube chrome). Live work cards for Stamps Steel, Bottom View Farm, and Roux's.

```
python scripts/build_site.py
```

Regenerates pages from `scripts/build_site.py`. Do not invent prices, clients, or quotes.
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
