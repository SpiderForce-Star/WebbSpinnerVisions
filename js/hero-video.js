/**
 * Hero video — YouTube embed, muted autoplay + unmute toggle
 */
(function () {
  'use strict';

  const VIDEO_ID = '8nsN5ESSrY0';
  const iframe = document.getElementById('hero-video');
  const muteBtn = document.getElementById('hero-mute-btn');
  const media = document.getElementById('hero-video-fullscreen-target');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!iframe || !media) return;

  const baseParams = {
    autoplay: reducedMotion ? '0' : '1',
    mute: '1',
    loop: '1',
    playlist: VIDEO_ID,
    controls: '1',
    rel: '0',
    playsinline: '1',
    modestbranding: '1',
    enablejsapi: '1'
  };

  const buildSrc = (muted = true) => {
    const params = { ...baseParams, mute: muted ? '1' : '0' };
    const query = Object.entries(params)
      .map(([key, value]) => `${key}=${value}`)
      .join('&');
    return `https://www.youtube-nocookie.com/embed/${VIDEO_ID}?${query}`;
  };

  const setMuteIcon = muted => {
    if (!muteBtn) return;
    muteBtn.setAttribute('aria-label', muted ? 'Unmute video' : 'Mute video');
    muteBtn.setAttribute('aria-pressed', muted ? 'true' : 'false');
    const icon = muteBtn.querySelector('i');
    if (icon) icon.className = muted ? 'fa-solid fa-volume-xmark' : 'fa-solid fa-volume-high';
  };

  iframe.src = buildSrc(true);
  media.classList.add('is-playing');
  setMuteIcon(true);

  muteBtn?.addEventListener('click', () => {
    const muted = iframe.src.includes('mute=1');
    iframe.src = buildSrc(!muted);
    setMuteIcon(!muted);
  });
})();