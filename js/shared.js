/**
 * Webb Spinner Visions — shared utilities
 */
(function () {
  'use strict';

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

  const highlightActiveNav = () => {
    const page = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('[data-nav-link]').forEach(link => {
      const href = link.getAttribute('href');
      if (href === page || (page === '' && href === 'index.html')) {
        link.classList.add('nav-active');
      }
    });
  };

  const loadPartials = async () => {
    const navSlot = document.getElementById('nav-placeholder');
    const footerSlot = document.getElementById('footer-placeholder');
    const tasks = [];

    if (navSlot) {
      tasks.push(fetch('nav.html').then(r => r.text()).then(html => { navSlot.innerHTML = html; }));
    }
    if (footerSlot) {
      tasks.push(fetch('footer.html').then(r => r.text()).then(html => { footerSlot.innerHTML = html; }));
    }

    await Promise.all(tasks);
    initMobileMenu();
    highlightActiveNav();
  };

  document.addEventListener('DOMContentLoaded', () => {
    const hasPartials = document.getElementById('nav-placeholder') || document.getElementById('footer-placeholder');

    if (hasPartials) {
      loadPartials().then(() => initLazyVideos());
    } else {
      initMobileMenu();
      highlightActiveNav();
      initLazyVideos();
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