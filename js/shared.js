/**
 * Webb Spinner Visions — shared utilities
 */
(function () {
  'use strict';

  const THEME_KEY = 'wsv-theme';

  const getPreferredTheme = () => {
    const stored = localStorage.getItem(THEME_KEY);
    if (stored === 'light' || stored === 'dark') return stored;
    return 'dark';
  };

  const applyTheme = theme => {
    document.documentElement.setAttribute('data-theme', theme);
    document.querySelectorAll('#theme-toggle i').forEach(icon => {
      icon.className = theme === 'light' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
    });
  };

  const initTheme = () => {
    applyTheme(getPreferredTheme());
    document.querySelectorAll('#theme-toggle').forEach(btn => {
      btn.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme') || 'dark';
        const next = current === 'light' ? 'dark' : 'light';
        localStorage.setItem(THEME_KEY, next);
        applyTheme(next);
      });
    });
  };

  const initMobileMenu = () => {
    const btn = document.getElementById('mobile-menu-btn');
    const closeBtn = document.getElementById('mobile-menu-close');
    const menu = document.getElementById('mobile-menu');
    const backdrop = document.getElementById('mobile-menu-backdrop');
    const links = document.querySelectorAll('.mobile-nav-link');

    if (!btn || !menu) return;

    const open = () => {
      menu.classList.add('open');
      backdrop?.classList.add('open');
      document.body.style.overflow = 'hidden';
      btn.setAttribute('aria-expanded', 'true');
      closeBtn?.focus();
    };

    const close = () => {
      menu.classList.remove('open');
      backdrop?.classList.remove('open');
      document.body.style.overflow = '';
      btn.setAttribute('aria-expanded', 'false');
    };

    btn.addEventListener('click', open);
    closeBtn?.addEventListener('click', close);
    backdrop?.addEventListener('click', close);
    links.forEach(link => link.addEventListener('click', close));

    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && menu.classList.contains('open')) close();
    });
  };

  const initLazyVideos = () => {
    const videos = document.querySelectorAll('video.lazy-video');

    if (!('IntersectionObserver' in window)) {
      videos.forEach(video => {
        const src = video.dataset.src;
        if (src) {
          video.querySelector('source')?.setAttribute('src', src);
          video.load();
        }
      });
      return;
    }

    const observer = new IntersectionObserver(
      entries => {
        entries.forEach(entry => {
          if (!entry.isIntersecting) return;
          const video = entry.target;
          const src = video.dataset.src;
          const source = video.querySelector('source');
          if (src && source && !source.getAttribute('src')) {
            source.setAttribute('src', src);
            video.load();
          }
          observer.unobserve(video);
        });
      },
      { rootMargin: '200px 0px', threshold: 0.1 }
    );

    videos.forEach(video => observer.observe(video));
  };

  const initLazyImages = () => {
    document.querySelectorAll('img[loading="lazy"]').forEach(img => {
      img.decoding = 'async';
    });
  };

  const highlightActiveNav = () => {
    const page = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('[data-nav-link]').forEach(link => {
      const href = link.getAttribute('href');
      if (href === page || (page === '' && href === 'index.html')) {
        link.classList.add('nav-active');
      }
    });
  };

  const initLazyEmbeds = () => {
    document.querySelectorAll('.video-embed-poster').forEach(btn => {
      btn.addEventListener('click', () => {
        const embed = btn.closest('.video-embed');
        const id = embed?.dataset.youtubeId;
        if (!id || embed.querySelector('iframe')) return;

        const iframe = document.createElement('iframe');
        iframe.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0`;
        iframe.title = btn.getAttribute('aria-label') || 'Embedded video';
        iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
        iframe.allowFullscreen = true;
        embed.appendChild(iframe);
        btn.remove();
      });
    });
  };

  const initStickyCta = () => {
    const bar = document.getElementById('sticky-cta');
    if (!bar) return;

    const contact = document.getElementById('contact');
    if (contact) {
      const observer = new IntersectionObserver(
        ([entry]) => {
          bar.classList.toggle('visible', !entry.isIntersecting && window.scrollY > 400);
        },
        { threshold: 0.1 }
      );
      observer.observe(contact);
      return;
    }

    const onScroll = () => {
      bar.classList.toggle('visible', window.scrollY > 400);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  };

  const initAfterPartials = () => {
    initTheme();
    initMobileMenu();
    highlightActiveNav();
    initLazyVideos();
    initLazyImages();
    initLazyEmbeds();
    initStickyCta();
  };

  const loadPartials = async () => {
    const navSlot = document.getElementById('nav-placeholder');
    const footerSlot = document.getElementById('footer-placeholder');
    const tasks = [];

    if (navSlot) {
      tasks.push(fetch('nav.html').then(r => r.text()).then(html => { navSlot.innerHTML = html; }));
    }
    if (footerSlot) {
      tasks.push(fetch('footer.html').then(r => r.text()).then(html => {
        footerSlot.innerHTML = html;
        const yearEl = document.getElementById('year');
        if (yearEl) yearEl.textContent = new Date().getFullYear();
      }));
    }

    await Promise.all(tasks);
    initAfterPartials();
  };

  document.addEventListener('DOMContentLoaded', () => {
    const hasPartials = document.getElementById('nav-placeholder') || document.getElementById('footer-placeholder');
    if (hasPartials) {
      loadPartials();
    } else {
      initAfterPartials();
    }
  });

  window.resetContactForm = () => {
    const form = document.getElementById('contact-form');
    const success = document.getElementById('form-success');
    if (form && success) {
      form.classList.remove('hidden');
      success.classList.add('hidden');
      form.reset();
    }
  };
})();
