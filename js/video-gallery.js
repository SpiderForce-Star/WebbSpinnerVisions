/**
 * YouTube video gallery — thumbnail cards + lightbox player
 */
(function () {
  'use strict';

  const lightbox = document.getElementById('video-lightbox');
  const iframe = document.getElementById('video-lightbox-iframe');
  const titleEl = document.getElementById('video-lightbox-title');
  const ytLink = document.getElementById('video-lightbox-yt');
  const closeBtn = document.getElementById('video-lightbox-close');

  if (!lightbox || !iframe) return;

  let lastFocus = null;

  const open = (id, title) => {
    lastFocus = document.activeElement;
    iframe.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0`;
    if (titleEl) titleEl.textContent = title;
    if (ytLink) {
      ytLink.href = `https://www.youtube.com/watch?v=${id}`;
      ytLink.textContent = 'Watch on YouTube';
    }
    lightbox.classList.remove('hidden');
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
    closeBtn?.focus();
  };

  const close = () => {
    lightbox.classList.add('hidden');
    lightbox.classList.remove('open');
    iframe.src = '';
    document.body.style.overflow = '';
    lastFocus?.focus();
  };

  document.querySelectorAll('.video-card[data-youtube-id]').forEach(card => {
    card.addEventListener('click', () => {
      open(card.dataset.youtubeId, card.dataset.videoTitle || 'Video');
    });
  });

  closeBtn?.addEventListener('click', close);
  lightbox.addEventListener('click', e => {
    if (e.target === lightbox) close();
  });

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && lightbox.classList.contains('open')) close();
  });
})();