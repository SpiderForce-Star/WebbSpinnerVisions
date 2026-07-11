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

  if (!document.documentElement.getAttribute('data-theme')) {
    document.documentElement.setAttribute('data-theme', getPreferredTheme());
  }

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
    const videos = document.querySelectorAll('video.lazy-video, video[data-src]');

    const loadVideo = video => {
      const src = video.dataset.src;
      const source = video.querySelector('source');
      if (src && source && !source.getAttribute('src')) {
        source.setAttribute('src', src);
        video.load();
      } else if (src && !video.getAttribute('src') && !source) {
        video.src = src;
        video.load();
      }
      video.classList.add('is-loaded');
    };

    if (!('IntersectionObserver' in window)) {
      videos.forEach(loadVideo);
      return;
    }

    const observer = new IntersectionObserver(
      entries => {
        entries.forEach(entry => {
          if (!entry.isIntersecting) return;
          loadVideo(entry.target);
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: '200px 0px', threshold: 0.05 }
    );

    videos.forEach(video => observer.observe(video));
  };

  const initLazyImages = () => {
    document.querySelectorAll('img').forEach(img => {
      if (!img.hasAttribute('loading') && !img.hasAttribute('fetchpriority')) {
        img.setAttribute('loading', 'lazy');
      }
      if (!img.hasAttribute('decoding')) {
        img.setAttribute('decoding', 'async');
      }
    });

    // Native lazy is preferred; enhance with IO for data-src images
    const deferred = document.querySelectorAll('img[data-src]');
    if (!deferred.length) return;

    const loadImg = img => {
      const src = img.dataset.src;
      if (src) {
        img.src = src;
        img.removeAttribute('data-src');
        img.classList.add('is-loaded');
      }
    };

    if (!('IntersectionObserver' in window)) {
      deferred.forEach(loadImg);
      return;
    }

    const observer = new IntersectionObserver(
      entries => {
        entries.forEach(entry => {
          if (!entry.isIntersecting) return;
          loadImg(entry.target);
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: '180px 0px', threshold: 0.01 }
    );

    deferred.forEach(img => observer.observe(img));
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
        iframe.loading = 'lazy';
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

  const initBackToTop = () => {
    const btn = document.getElementById('back-to-top');
    if (!btn) return;

    const toggle = () => {
      const show = window.scrollY > 480;
      btn.classList.toggle('is-visible', show);
      if (show) btn.removeAttribute('hidden');
      else btn.setAttribute('hidden', '');
    };

    btn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    window.addEventListener('scroll', toggle, { passive: true });
    toggle();
  };

  /** Floating Contact Us — appears after scrolling past hero */
  const initFloatingContact = () => {
    const btn = document.getElementById('floating-contact');
    if (!btn) return;

    // Point relative contact on homepage
    if (window.location.pathname.endsWith('/') || window.location.pathname.endsWith('index.html') || window.location.pathname === '') {
      btn.setAttribute('href', '#contact');
    }

    const hero =
      document.querySelector('.hero-landing') ||
      document.querySelector('.page-hero') ||
      document.querySelector('.cinematic-hero') ||
      document.getElementById('main');

    const contact = document.getElementById('contact');

    const update = () => {
      let pastHero = window.scrollY > 320;
      if (hero) {
        const rect = hero.getBoundingClientRect();
        pastHero = rect.bottom < 80;
      }

      let nearContact = false;
      if (contact) {
        const c = contact.getBoundingClientRect();
        nearContact = c.top < window.innerHeight * 0.85 && c.bottom > 0;
      }

      const show = pastHero && !nearContact;
      btn.classList.toggle('is-visible', show);
      if (show) btn.removeAttribute('hidden');
      else btn.setAttribute('hidden', '');
    };

    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update, { passive: true });
    update();
  };

  const initSmoothAnchors = () => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', e => {
        const href = anchor.getAttribute('href');
        if (!href || href === '#') return;
        const target = document.querySelector(href);
        if (!target) return;
        e.preventDefault();
        const top = target.getBoundingClientRect().top + window.scrollY - 80;
        window.scrollTo({ top, behavior: 'smooth' });
      });
    });
  };

  const initReveal = () => {
    const revealEls = document.querySelectorAll('.reveal');
    if (!revealEls.length) return;

    if (!('IntersectionObserver' in window)) {
      revealEls.forEach(el => el.classList.add('visible'));
      return;
    }

    const observer = new IntersectionObserver(
      entries => {
        entries.forEach(entry => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );

    revealEls.forEach(el => observer.observe(el));
  };

  const initPackageCheckmarks = () => {
    const cards = document.querySelectorAll('.package-card');
    if (!cards.length || !('IntersectionObserver' in window)) {
      cards.forEach(c => c.classList.add('checks-animate'));
      return;
    }

    const observer = new IntersectionObserver(
      entries => {
        entries.forEach(entry => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('checks-animate');
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.2 }
    );

    cards.forEach(card => observer.observe(card));
  };

  const initAfterPartials = () => {
    initTheme();
    initMobileMenu();
    highlightActiveNav();
    initLazyVideos();
    initLazyImages();
    initLazyEmbeds();
    initStickyCta();
    initBackToTop();
    initFloatingContact();
    initSmoothAnchors();
    initReveal();
    initPackageCheckmarks();
  };

  const loadPartials = async () => {
    const navSlot = document.getElementById('nav-placeholder');
    const footerSlot = document.getElementById('footer-placeholder');
    const tasks = [];

    if (navSlot) {
      tasks.push(
        fetch('nav.html')
          .then(r => r.text())
          .then(html => {
            navSlot.innerHTML = html;
          })
      );
    }
    if (footerSlot) {
      tasks.push(
        fetch('footer.html')
          .then(r => r.text())
          .then(html => {
            footerSlot.innerHTML = html;
            const yearEl = document.getElementById('year');
            if (yearEl) yearEl.textContent = new Date().getFullYear();
          })
      );
    }

    await Promise.all(tasks);
    initAfterPartials();
  };

  document.addEventListener('DOMContentLoaded', () => {
    const hasPartials =
      document.getElementById('nav-placeholder') || document.getElementById('footer-placeholder');
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
