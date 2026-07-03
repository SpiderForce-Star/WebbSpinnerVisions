/**
 * Hero video — immersive top-stage player, muted autoplay + unmute
 * Optimized for iOS Safari and Android mobile autoplay policies
 */
(function () {
  'use strict';

  const VIDEO_ID = '_mEvE69qwjY';
  const MP4_SRC = 'videos/wsv-top-entrance.mp4';
  const video = document.getElementById('hero-video');
  const fallback = document.getElementById('hero-video-fallback');
  const muteBtn = document.getElementById('hero-mute-btn');
  const media = document.getElementById('hero-video-fullscreen-target');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!video || !media) return;

  let usingIframe = false;
  let playAttempts = 0;
  const MAX_PLAY_ATTEMPTS = 10;

  video.defaultMuted = true;
  video.muted = true;
  video.setAttribute('muted', '');
  video.playsInline = true;
  video.setAttribute('playsinline', '');
  video.setAttribute('webkit-playsinline', '');

  const markPlaying = () => {
    media.classList.add('is-playing');
    video.removeAttribute('poster');
  };

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
    video.pause();
    video.style.display = 'none';
    fallback.hidden = false;
    fallback.innerHTML = '';
    const iframe = document.createElement('iframe');
    iframe.src = `https://www.youtube-nocookie.com/embed/${VIDEO_ID}?autoplay=1&mute=1&loop=1&playlist=${VIDEO_ID}&controls=0&rel=0&playsinline=1&modestbranding=1&enablejsapi=1`;
    iframe.title = video.getAttribute('aria-label') || 'WSV Top Entrance Video';
    iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    iframe.allowFullscreen = true;
    iframe.className = 'hero-video-iframe-fallback';
    fallback.appendChild(iframe);
    media.classList.add('is-playing');
  };

  const tryPlay = () => {
    if (usingIframe || reducedMotion) return;

    if (playAttempts >= MAX_PLAY_ATTEMPTS) {
      loadYouTubeFallback();
      return;
    }

    playAttempts += 1;
    video.defaultMuted = true;
    video.muted = true;

    const promise = video.play();
    if (promise && typeof promise.then === 'function') {
      promise
        .then(() => markPlaying())
        .catch(() => {
          if (playAttempts >= 4) {
            loadYouTubeFallback();
          } else {
            window.setTimeout(tryPlay, 250 * playAttempts);
          }
        });
    }
  };

  const verifySource = async () => {
    try {
      const res = await fetch(MP4_SRC, { method: 'HEAD', cache: 'no-store' });
      if (!res.ok) {
        loadYouTubeFallback();
        return false;
      }
      return true;
    } catch {
      return true;
    }
  };

  video.addEventListener('error', loadYouTubeFallback);
  video.addEventListener('loadedmetadata', tryPlay);
  video.addEventListener('canplay', tryPlay);
  video.addEventListener('playing', markPlaying);

  document.addEventListener('visibilitychange', () => {
    if (!document.hidden && !usingIframe && !reducedMotion) tryPlay();
  });

  window.addEventListener('pageshow', e => {
    if (e.persisted && !usingIframe && !reducedMotion) tryPlay();
  });

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting && !usingIframe && !reducedMotion) tryPlay();
        });
      },
      { threshold: 0.2 }
    );
    observer.observe(media);
  }

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

  if (reducedMotion) {
    video.removeAttribute('autoplay');
    video.pause();
    return;
  }

  verifySource().then(ok => {
    if (ok && !usingIframe) tryPlay();
  });
})();