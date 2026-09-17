/* Webb Spinner Visions — studio interactions */
(function () {
  "use strict";

  const $ = (sel, root) => (root || document).querySelector(sel);
  const $$ = (sel, root) => Array.from((root || document).querySelectorAll(sel));

  const PACKAGE_MAP = {
    launch: "Launch",
    grow: "Grow",
    heavy: "Heavy",
    visual: "Visual sales",
    promo: "Visual sales",
    software: "Software",
    ai: "AI",
    other: "Not sure",
  };

  function initNav() {
    const header = $(".site-header");
    const btn = $(".menu-btn");
    const drawer = $(".drawer");
    const onScroll = () => header?.classList.toggle("is-scrolled", window.scrollY > 12);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });

    if (!btn || !drawer) return;
    const setOpen = (open) => {
      drawer.classList.toggle("is-open", open);
      header?.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.classList.toggle("menu-lock", open);
      drawer.hidden = !open;
    };
    setOpen(false);
    btn.addEventListener("click", () => setOpen(!drawer.classList.contains("is-open")));
    $$("a", drawer).forEach((a) => a.addEventListener("click", () => setOpen(false)));
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") setOpen(false);
    });
  }

  function initHero() {
    const video = $(".hero-video");
    const muteBtn = $(".mute-btn");
    if (!video) return;

    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    video.muted = true;
    video.playsInline = true;
    video.setAttribute("playsinline", "");
    video.setAttribute("webkit-playsinline", "");

    const play = () => {
      const p = video.play();
      if (p && p.catch) p.catch(() => {});
    };

    if (reduced) {
      video.pause();
      video.removeAttribute("autoplay");
      return;
    }

    play();
    document.addEventListener("visibilitychange", () => {
      if (document.hidden) video.pause();
      else play();
    });

    if (!muteBtn) return;
    const icon = () => {
      muteBtn.setAttribute("aria-label", video.muted ? "Unmute film" : "Mute film");
      muteBtn.setAttribute("aria-pressed", video.muted ? "true" : "false");
      muteBtn.innerHTML = video.muted
        ? '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3 3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4 9.91 6.09 12 8.18V4z"/></svg>'
        : '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>';
    };
    icon();
    muteBtn.addEventListener("click", () => {
      video.muted = !video.muted;
      if (!video.muted) play();
      icon();
    });
  }

  function applyPackage(value) {
    const select = $("#package");
    if (!select || !value) return;
    const mapped = PACKAGE_MAP[value] || value;
    const match = Array.from(select.options).find(
      (o) => o.value === mapped || o.value.toLowerCase() === String(value).toLowerCase()
    );
    if (match) select.value = match.value;
    try {
      sessionStorage.setItem("wsv-package", match ? match.value : mapped);
    } catch (e) {}
  }

  function initPackagePrefill() {
    const params = new URLSearchParams(window.location.search);
    const fromUrl = params.get("package");
    let stored = null;
    try {
      stored = sessionStorage.getItem("wsv-package");
    } catch (e) {}
    if (fromUrl) applyPackage(fromUrl);
    else if (stored) applyPackage(stored);

    $$("[data-package]").forEach((el) => {
      el.addEventListener("click", () => applyPackage(el.getAttribute("data-package")));
    });
  }

  function initForm() {
    const form = $("#contact-form");
    if (!form) return;
    if (new URLSearchParams(window.location.search).get("sent") === "true") {
      form.classList.add("is-hidden");
      $("#form-success")?.classList.add("is-visible");
    }
    form.addEventListener("submit", () => {
      const email = form.querySelector('input[name="email"]');
      const replyto = form.querySelector('input[name="_replyto"]');
      if (email && replyto) replyto.value = email.value.trim();
    });
  }

  function initLightbox() {
    const box = $("#lightbox");
    const frame = $("#lightbox-frame");
    const title = $("#lightbox-title");
    const yt = $("#lightbox-yt");
    const close = $("#lightbox-close");
    if (!box || !frame) return;

    let last = null;
    const open = (id, name) => {
      last = document.activeElement;
      frame.innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0&modestbranding=1" title="${name}" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>`;
      if (title) title.textContent = name;
      if (yt) {
        yt.href = `https://www.youtube.com/watch?v=${id}`;
        yt.hidden = false;
      }
      box.classList.add("is-open");
      box.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";
      close?.focus();
    };
    const shut = () => {
      box.classList.remove("is-open");
      box.setAttribute("aria-hidden", "true");
      frame.innerHTML = "";
      document.body.style.overflow = "";
      last?.focus();
    };

    $$("[data-youtube]").forEach((btn) => {
      btn.addEventListener("click", () => open(btn.dataset.youtube, btn.dataset.title || "Film"));
    });
    close?.addEventListener("click", shut);
    box.addEventListener("click", (e) => {
      if (e.target === box) shut();
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && box.classList.contains("is-open")) shut();
    });
  }

  function initHangar() {
    const enter = $("#hangar-enter");
    const hangar = $("#hangar");
    const game = $("#game-frame");
    const status = $("#hangar-status");
    const iframe = $("#sf5");
    if (!enter || !hangar || !game) return;

    const lines = $$("#sys-list li");
    enter.addEventListener("click", () => {
      enter.disabled = true;
      if (status) status.textContent = "Hangar handshake in progress.";
      lines.forEach((li, i) => {
        window.setTimeout(() => li.classList.add("is-on"), 280 * (i + 1));
      });
      window.setTimeout(() => {
        hangar.hidden = true;
        game.classList.add("is-live");
        if (iframe && !iframe.getAttribute("src")) {
          iframe.src = iframe.dataset.src || "https://spiderforce-star.github.io/Spider-Force-5/";
        }
        game.scrollIntoView({ behavior: "smooth", block: "start" });
      }, 280 * (lines.length + 2) + 400);
    });
  }

  function initSticky() {
    const sticky = $(".sticky-contact");
    if (!sticky) return;
    const contact = $("#contact");
    const update = () => {
      const past = window.scrollY > 500;
      let near = false;
      if (contact) {
        const r = contact.getBoundingClientRect();
        near = r.top < window.innerHeight * 0.9 && r.bottom > 0;
      }
      sticky.classList.toggle("is-visible", past && !near);
    };
    window.addEventListener("scroll", update, { passive: true });
    update();
  }

  function initYear() {
    $$("[data-year]").forEach((el) => {
      el.textContent = String(new Date().getFullYear());
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    initNav();
    initHero();
    initPackagePrefill();
    initForm();
    initLightbox();
    initHangar();
    initSticky();
    initYear();
  });
})();
