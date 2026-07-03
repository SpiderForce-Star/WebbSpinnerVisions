/**
 * Hero video — YouTube IFrame API + custom cinematic controls
 */
(function () {
  'use strict';

  const VIDEO_ID = '_mEvE69qwjY';
  const playerEl = document.getElementById('hero-yt-player');
  const mount = playerEl?.closest('.hero-yt-player-mount');
  if (!playerEl) return;

  const playBtn = document.getElementById('hero-play-btn');
  const muteBtn = document.getElementById('hero-mute-btn');
  const fsBtn = document.getElementById('hero-fullscreen-btn');
  const fsTarget = document.getElementById('hero-video-fullscreen-target');
  const cinema = document.getElementById('hero-video-cinema');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  let player = null;
  let isPlaying = true;
  let isMuted = true;

  const setPlayIcon = playing => {
    if (!playBtn) return;
    playBtn.setAttribute('aria-label', playing ? 'Pause video' : 'Play video');
    playBtn.setAttribute('aria-pressed', playing ? 'true' : 'false');
    const icon = playBtn.querySelector('i');
    if (icon) icon.className = playing ? 'fa-solid fa-pause' : 'fa-solid fa-play';
  };

  const setMuteIcon = muted => {
    if (!muteBtn) return;
    muteBtn.setAttribute('aria-label', muted ? 'Unmute video' : 'Mute video');
    muteBtn.setAttribute('aria-pressed', muted ? 'true' : 'false');
    const icon = muteBtn.querySelector('i');
    if (icon) icon.className = muted ? 'fa-solid fa-volume-xmark' : 'fa-solid fa-volume-high';
  };

  const setFsIcon = expanded => {
    if (!fsBtn) return;
    fsBtn.setAttribute('aria-label', expanded ? 'Exit fullscreen' : 'Enter fullscreen');
    const icon = fsBtn.querySelector('i');
    if (icon) icon.className = expanded ? 'fa-solid fa-compress' : 'fa-solid fa-expand';
  };

  const onPlayerReady = event => {
    event.target.playVideo();
    mount?.classList.add('is-ready');
    cinema?.classList.add('is-live');
    setPlayIcon(true);
    setMuteIcon(true);
  };

  const onPlayerStateChange = event => {
    if (event.data === YT.PlayerState.PLAYING) {
      isPlaying = true;
      setPlayIcon(true);
    } else if (event.data === YT.PlayerState.PAUSED) {
      isPlaying = false;
      setPlayIcon(false);
    } else if (event.data === YT.PlayerState.ENDED) {
      event.target.playVideo();
    }
  };

  const initPlayer = () => {
    player = new YT.Player('hero-yt-player', {
      videoId: VIDEO_ID,
      playerVars: {
        autoplay: 1,
        mute: 1,
        loop: 1,
        playlist: VIDEO_ID,
        controls: 0,
        rel: 0,
        playsinline: 1,
        modestbranding: 1,
        iv_load_policy: 3,
        disablekb: 1,
        fs: 0,
        origin: window.location.origin
      },
      events: {
        onReady: onPlayerReady,
        onStateChange: onPlayerStateChange
      }
    });
  };

  const loadYouTubeApi = () => {
    if (window.YT && window.YT.Player) {
      initPlayer();
      return;
    }

    const prev = window.onYouTubeIframeAPIReady;
    window.onYouTubeIframeAPIReady = () => {
      if (typeof prev === 'function') prev();
      initPlayer();
    };

    if (!document.querySelector('script[src*="youtube.com/iframe_api"]')) {
      const tag = document.createElement('script');
      tag.src = 'https://www.youtube.com/iframe_api';
      tag.async = true;
      document.head.appendChild(tag);
    }
  };

  playBtn?.addEventListener('click', () => {
    if (!player?.getPlayerState) return;
    const state = player.getPlayerState();
    if (state === YT.PlayerState.PLAYING) {
      player.pauseVideo();
      isPlaying = false;
      setPlayIcon(false);
    } else {
      player.playVideo();
      isPlaying = true;
      setPlayIcon(true);
    }
  });

  muteBtn?.addEventListener('click', () => {
    if (!player?.isMuted) return;
    if (player.isMuted()) {
      player.unMute();
      player.setVolume(80);
      isMuted = false;
      setMuteIcon(false);
    } else {
      player.mute();
      isMuted = true;
      setMuteIcon(true);
    }
  });

  const toggleFullscreen = () => {
    const el = fsTarget;
    if (!el) return;
    if (!document.fullscreenElement) {
      (el.requestFullscreen || el.webkitRequestFullscreen)?.call(el);
    } else {
      (document.exitFullscreen || document.webkitExitFullscreen)?.call(document);
    }
  };

  fsBtn?.addEventListener('click', toggleFullscreen);

  document.addEventListener('fullscreenchange', () => {
    setFsIcon(!!document.fullscreenElement);
    fsTarget?.classList.toggle('is-fullscreen', !!document.fullscreenElement);
  });

  if (reducedMotion) {
    if (mount) mount.style.display = 'none';
    cinema?.classList.remove('hero-video-cinema--enter');
    return;
  }

  setTimeout(() => cinema?.classList.add('is-live'), 1300);

  loadYouTubeApi();
})();