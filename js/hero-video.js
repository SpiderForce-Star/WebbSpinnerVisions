/**
 * Hero video — lazy YouTube facade, muted autoplay on activate
 */
(function () {
  'use strict';

  const VIDEO_ID = '8nsN5ESSrY0';
  const EMBED_BASE = 'https://www.youtube-nocookie.com/embed/';

  const facade = document.getElementById('hero-youtube-facade');
  const playBtn = document.getElementById('hero-play-btn');
  const container = document.getElementById('hero-video-fallback');
  const muteBtn = document.getElementById('hero-mute-btn');
  const media = document.getElementById('hero-video-fullscreen-target');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!facade || !container || !media) return;

  let iframe = null;
  let activated = false;
  let isMuted = true;

  const buildSrc = muted => {
    const params = new URLSearchParams({
      autoplay: reducedMotion ? '0' : '1',
      mute: muted ? '1' : '0',
      loop: '1',
      playlist: VIDEO_ID,
      playsinline: '1',
      rel: '0',
      modestbranding: '1',
      controls: '1'
    });
    return `${EMBED_BASE}${VIDEO_ID}?${params.toString()}`;
  };

  const setMuteIcon = muted => {
    if (!muteBtn) return;
    muteBtn.setAttribute('aria-label', muted ? 'Unmute video' : 'Mute video');
    muteBtn.setAttribute('aria-pressed', muted ? 'true' : 'false');
    const icon = muteBtn.querySelector('i');
    if (icon) icon.className = muted ? 'fa-solid fa-volume-xmark' : 'fa-solid fa-volume-high';
  };

  const hideFacade = () => {
    facade.classList.add('is-hidden');
    facade.setAttribute('aria-hidden', 'true');
    muteBtn?.removeAttribute('hidden');
    media.classList.add('is-playing');
  };

  const activate = () => {
    if (activated) return;
    activated = true;
    facade.classList.add('is-loading');

    container.hidden = false;
    iframe = document.createElement('iframe');
    iframe.id = 'hero-video';
    iframe.className = 'hero-landing-iframe';
    iframe.title = 'Webb Spinner Visions — cinematic video showcase';
    iframe.loading = 'lazy';
    iframe.setAttribute(
      'allow',
      'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture'
    );
    iframe.allowFullscreen = true;
    iframe.src = buildSrc(isMuted);

    iframe.addEventListener('load', hideFacade, { once: true });
    container.appendChild(iframe);

    setMuteIcon(isMuted);

    window.setTimeout(hideFacade, 1200);
  };

  playBtn?.addEventListener('click', activate);

  muteBtn?.addEventListener('click', () => {
    if (!iframe) return;
    isMuted = !isMuted;
    iframe.src = buildSrc(isMuted);
    setMuteIcon(isMuted);
  });

  if (!reducedMotion && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            observer.disconnect();
            const schedule = cb =>
              window.requestIdleCallback
                ? window.requestIdleCallback(cb, { timeout: 2000 })
                : window.setTimeout(cb, 600);
            schedule(() => activate());
          }
        });
      },
      { threshold: 0.15, rootMargin: '80px' }
    );
    observer.observe(media);
  }
})();