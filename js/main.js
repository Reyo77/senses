(function () {
  var root = document.documentElement;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* theme */
  var saved = null;
  try { saved = localStorage.getItem('theme'); } catch (e) {}
  var theme = saved || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  root.setAttribute('data-theme', theme);
  var tbtn = $('#theme');
  if (tbtn) tbtn.addEventListener('click', function () {
    theme = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', theme);
    try { localStorage.setItem('theme', theme); } catch (e) {}
    tbtn.setAttribute('aria-pressed', theme === 'dark');
  });

  /* mobile menu */
  var burger = $('#burger'), menu = $('#menu');
  if (burger) burger.addEventListener('click', function () {
    var o = menu.classList.toggle('open');
    burger.setAttribute('aria-expanded', o);
  });
  $$('#menu a').forEach(function (a) { a.addEventListener('click', function () { menu.classList.remove('open'); burger.setAttribute('aria-expanded', false); }); });
  $$('.dd>button').forEach(function (b) { b.addEventListener('click', function () { b.parentNode.classList.toggle('open'); }); });

  /* scroll effects */
  var nav = $('.nav'), bar = $('#progress'), top = $('.to-top');
  function onScroll() {
    var y = scrollY, h = document.documentElement.scrollHeight - innerHeight;
    if (nav) nav.classList.toggle('scrolled', y > 10);
    if (bar) bar.style.width = (h > 0 ? y / h * 100 : 0) + '%';
    if (top) top.classList.toggle('show', y > 700);
  }
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* reveal */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: .12, rootMargin: '0px 0px -40px 0px' });
    $$('.rv').forEach(function (el) { io.observe(el); });
    setTimeout(function () { $$('.rv').forEach(function (el) { var b = el.getBoundingClientRect(); if (b.top < innerHeight && b.bottom > 0) { el.classList.add('in'); io.unobserve(el); } }); }, 60);
  } else { $$('.rv').forEach(function (el) { el.classList.add('in'); }); }

  /* counters */
  function count(el) {
    var end = parseFloat(el.dataset.to), suf = el.dataset.suf || '', t0 = null, dur = 1600;
    function f(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1), e = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(end * e).toLocaleString('en-CA') + suf;
      if (p < 1) requestAnimationFrame(f);
    }
    requestAnimationFrame(f);
    setTimeout(function () { el.textContent = end.toLocaleString('en-CA') + suf; }, dur + 400);
  }
  if ('IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { count(e.target); co.unobserve(e.target); } });
    }, { threshold: .6 });
    $$('[data-to]').forEach(function (el) { co.observe(el); });
  }

  /* team bio dialog */
  var dlg = $('#bio');
  if (dlg) {
    $$('[data-bio]').forEach(function (b) {
      b.addEventListener('click', function () {
        var t = document.getElementById(b.dataset.bio);
        $('#bio-body').innerHTML = '';
        $('#bio-body').appendChild(t.content.cloneNode(true));
        dlg.showModal();
      });
    });
    dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
    $$('.dlg-x', dlg).forEach(function (x) { x.addEventListener('click', function () { dlg.close(); }); });
  }

  /* highlight today's hours */
  var dow = String(new Date().getDay());
  $$('.hours tr').forEach(function (tr) { if (tr.dataset.d === dow) tr.classList.add('today'); });

  /* footer year */
  $$('.yr').forEach(function (n) { n.textContent = new Date().getFullYear(); });
})();
