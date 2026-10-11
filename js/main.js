(function () {
  // header scroll state
  var header = document.querySelector('.site-header');
  function onScroll() { header.classList.toggle('scrolled', window.scrollY > 40); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
      if (open) header.classList.add('scrolled');
      else onScroll();
    });
  }

  // lightbox
  var lb = document.getElementById('lightbox');
  if (!lb) return;
  var lbImg = lb.querySelector('img');
  var items = Array.prototype.slice.call(document.querySelectorAll('[data-lightbox]'));
  var idx = -1;
  function show(i) {
    if (!items.length) return;
    idx = (i + items.length) % items.length;
    lbImg.src = items[idx].getAttribute('href');
    lb.hidden = false;
    document.body.style.overflow = 'hidden';
  }
  function hide() { lb.hidden = true; lbImg.src = ''; document.body.style.overflow = ''; }
  items.forEach(function (a, i) {
    a.addEventListener('click', function (e) { e.preventDefault(); show(i); });
  });
  lb.querySelector('.lb-close').addEventListener('click', hide);
  lb.querySelector('.lb-prev').addEventListener('click', function () { show(idx - 1); });
  lb.querySelector('.lb-next').addEventListener('click', function () { show(idx + 1); });
  lb.addEventListener('click', function (e) { if (e.target === lb) hide(); });
  document.addEventListener('keydown', function (e) {
    if (lb.hidden) return;
    if (e.key === 'Escape') hide();
    if (e.key === 'ArrowLeft') show(idx - 1);
    if (e.key === 'ArrowRight') show(idx + 1);
  });
})();
