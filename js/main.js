document.addEventListener('DOMContentLoaded', () => {
  const params = new URLSearchParams(window.location.search);
  const packageMap = {
    starter: 'Starter Website Package ($800)',
    cinematic: 'Cinematic Website Package ($1,000)',
    video: 'Video / Logo Animation only',
    marketing: 'Marketing support'
  };

  if (params.get('sent') === 'true') {
    const form = document.getElementById('contact-form');
    const success = document.getElementById('form-success');
    if (form && success) {
      form.classList.add('hidden');
      success.classList.remove('hidden');
      history.replaceState({}, '', `${window.location.pathname}#contact`);
    }
  }

  const nav = document.getElementById('navbar');
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileMenuClose = document.getElementById('mobile-menu-close');
  const mobileMenuBackdrop = document.getElementById('mobile-menu-backdrop');
  const mobileLinks = document.querySelectorAll('.mobile-nav-link');
  const yearEl = document.getElementById('year');

  if (yearEl) yearEl.textContent = new Date().getFullYear();

  const handleScroll = () => {
    if (!nav) return;
    nav.classList.toggle('nav-scrolled', window.scrollY > 40);
  };
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  const openMenu = () => {
    mobileMenu?.classList.add('open');
    mobileMenuBackdrop?.classList.add('open');
    document.body.style.overflow = 'hidden';
    mobileMenuBtn?.setAttribute('aria-expanded', 'true');
  };

  const closeMenu = () => {
    mobileMenu?.classList.remove('open');
    mobileMenuBackdrop?.classList.remove('open');
    document.body.style.overflow = '';
    mobileMenuBtn?.setAttribute('aria-expanded', 'false');
  };

  mobileMenuBtn?.addEventListener('click', openMenu);
  mobileMenuClose?.addEventListener('click', closeMenu);
  mobileMenuBackdrop?.addEventListener('click', closeMenu);
  mobileLinks.forEach(link => link.addEventListener('click', closeMenu));

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeMenu();
  });

  const revealEls = document.querySelectorAll('.reveal');
  const revealObserver = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
  );
  revealEls.forEach(el => revealObserver.observe(el));

  const lazyVideos = document.querySelectorAll('video.lazy-video');
  if ('IntersectionObserver' in window) {
    const videoObserver = new IntersectionObserver(
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
          videoObserver.unobserve(video);
        });
      },
      { rootMargin: '200px 0px', threshold: 0.1 }
    );
    lazyVideos.forEach(v => videoObserver.observe(v));
  }

  document.querySelectorAll('.portfolio-item').forEach(item => {
    const video = item.querySelector('video');
    const playBtn = item.querySelector('.play-btn');

    if (video && playBtn) {
      playBtn.style.pointerEvents = 'auto';
      playBtn.addEventListener('click', e => {
        e.stopPropagation();
        if (video.paused) video.play();
        else video.pause();
      });
      video.addEventListener('play', () => { playBtn.style.opacity = '0.15'; });
      video.addEventListener('pause', () => { playBtn.style.opacity = ''; });
    }
  });

  const filterBtns = document.querySelectorAll('.filter-btn');
  const portfolioItems = document.querySelectorAll('.portfolio-item');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.dataset.filter;
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      portfolioItems.forEach(item => {
        const category = item.dataset.category;
        const show = filter === 'all' || category === filter;
        item.style.display = show ? '' : 'none';
      });
    });
  });

  const projectTypeSelect = document.getElementById('project_type');
  const packageFromUrl = params.get('package');
  if (packageFromUrl && projectTypeSelect && packageMap[packageFromUrl]) {
    projectTypeSelect.value = packageMap[packageFromUrl];
  }

  document.querySelectorAll('[data-package]').forEach(link => {
    link.addEventListener('click', () => {
      if (!projectTypeSelect) return;
      const pkg = link.dataset.package;
      if (packageMap[pkg]) projectTypeSelect.value = packageMap[pkg];
    });
  });

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const href = anchor.getAttribute('href');
      if (href === '#') return;
      const target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      const top = target.getBoundingClientRect().top + window.scrollY - 80;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });
});
