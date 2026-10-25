(() => {
  'use strict';

  const menuToggle = document.querySelector('.menu-toggle');
  const primaryNav = document.querySelector('#primary-nav');
  const filterButtons = [...document.querySelectorAll('[data-filter]')];
  const projectCards = [...document.querySelectorAll('.project-card')];
  const filterEmpty = document.querySelector('#filter-empty');
  const progressBar = document.querySelector('#reading-progress-bar');
  const yearLabel = document.querySelector('#current-year');

  if (yearLabel) yearLabel.textContent = String(new Date().getFullYear());

  function closeMenu() {
    if (!menuToggle || !primaryNav) return;
    menuToggle.setAttribute('aria-expanded', 'false');
    menuToggle.setAttribute('aria-label', 'Open navigation');
    primaryNav.classList.remove('is-open');
    document.body.classList.remove('menu-open');
  }

  menuToggle?.addEventListener('click', () => {
    const opening = menuToggle.getAttribute('aria-expanded') !== 'true';
    menuToggle.setAttribute('aria-expanded', String(opening));
    menuToggle.setAttribute('aria-label', opening ? 'Close navigation' : 'Open navigation');
    primaryNav?.classList.toggle('is-open', opening);
    document.body.classList.toggle('menu-open', opening);
  });

  primaryNav?.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeMenu();
  });

  // Release the mobile scroll lock if the viewport grows past the mobile breakpoint.
  window.addEventListener('resize', () => {
    if (window.innerWidth > 680) closeMenu();
  });

  filterButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const selected = button.dataset.filter || 'all';
      let visibleCount = 0;

      filterButtons.forEach((filterButton) => {
        const isActive = filterButton === button;
        filterButton.classList.toggle('is-active', isActive);
        filterButton.setAttribute('aria-pressed', String(isActive));
      });

      projectCards.forEach((card) => {
        const categories = (card.dataset.category || '').split(/\s+/).filter(Boolean);
        const show = selected === 'all' || categories.includes(selected);
        card.hidden = !show;
        if (show) visibleCount += 1;
      });

      if (filterEmpty) filterEmpty.hidden = visibleCount !== 0;
    });
  });

  let scrollQueued = false;
  function updateProgress() {
    if (!progressBar || scrollQueued) return;
    scrollQueued = true;
    window.requestAnimationFrame(() => {
      const root = document.documentElement;
      const scrollable = root.scrollHeight - root.clientHeight;
      const amount = scrollable > 0 ? (root.scrollTop / scrollable) * 100 : 0;
      progressBar.style.width = `${Math.min(100, Math.max(0, amount))}%`;
      scrollQueued = false;
    });
  }
  window.addEventListener('scroll', updateProgress, { passive: true });
  window.addEventListener('resize', updateProgress, { passive: true });
  updateProgress();
})();
