/**
 * Hero video — full-bleed landing background, muted autoplay + unmute
 */
(function () {
  'use strict';

  const VIDEO_ID = '_mEvE69qwjY';
  const video = document.getElementById('hero-video');
  const fallback = document.getElementById('hero-video-fallback');
  const muteBtn = document.getElementById('hero-mute-btn');
  const media = document.getElementById('hero-video-fullscreen-target');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!video || !media) return;

  let usingIframe = false;

  const setMuteIcon = muted => {
    if (!muteBtn) return;
    muteBtn.setAttribute('aria-label', muted ? 'Unmute video' : 'Mute video');
    muteBtn.setAttribute('aria-pressed', muted ? 'true' : 'false');
    const icon = muteBtn.querySelector('i');
    if (icon) icon.className = muted ? 'fa-solid fa-volume-xmark' : 'fa-solid fa-volume-high';
  };

  const loadYouTubeFallback = () => {
    if (!fallback || usingIframe) return;
    usingIframe = true;
    video.style.display = 'none';
    fallback.hidden = false;
    fallback.innerHTML = '';
    const iframe = document.createElement('iframe');
    iframe.src = `https://www.youtube-nocookie.com/embed/${VIDEO_ID}?autoplay=1&mute=1&loop=1&playlist=${VIDEO_ID}&controls=0&rel=0&playsinline=1&modestbranding=1`;
    iframe.title = video.getAttribute('aria-label') || 'WSV Top Entrance Video';
    iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
    iframe.allowFullscreen = true;
    iframe.className = 'hero-video-iframe-fallback';
    fallback.appendChild(iframe);
  };

  const tryPlay = () => {
    const p = video.play();
    if (p && typeof p.catch === 'function') {
      p.catch(() => loadYouTubeFallback());
    }
  };

  video.addEventListener('error', loadYouTubeFallback);

  video.addEventListener('loadeddata', () => {
    media.classList.add('is-playing');
    tryPlay();
  });

  if (reducedMotion) {
    video.removeAttribute('autoplay');
    video.pause();
    return;
  }

  tryPlay();

  muteBtn?.addEventListener('click', () => {
    if (usingIframe) {
      const iframe = fallback?.querySelector('iframe');
      if (!iframe) return;
      const muted = iframe.src.includes('mute=1');
      iframe.src = muted
        ? iframe.src.replace('mute=1', 'mute=0')
        : iframe.src.replace('mute=0', 'mute=1');
      setMuteIcon(!muted);
      return;
    }
    video.muted = !video.muted;
    setMuteIcon(video.muted);
  });

  setMuteIcon(true);
})();