// ============ ANSHU PROPERTIES — SHARED INTERACTIVE BEHAVIOR ============
document.addEventListener('DOMContentLoaded', () => {

  /* Sticky header shadow */
  const header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', () => {
      header.classList.toggle('scrolled', window.scrollY > 10);
    });
  }

  /* Mobile menu toggle */
  const menuToggle = document.querySelector('.menu-toggle');
  const navMobile = document.querySelector('.nav-mobile');
  if (menuToggle && navMobile) {
    menuToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      navMobile.classList.toggle('open');
      navMobile.classList.toggle('show');
      const isOpen = navMobile.classList.contains('open') || navMobile.classList.contains('show');
      menuToggle.setAttribute('aria-expanded', isOpen);
    });

    document.addEventListener('click', (e) => {
      if (!navMobile.contains(e.target) && !menuToggle.contains(e.target)) {
        navMobile.classList.remove('open', 'show');
        menuToggle.setAttribute('aria-expanded', 'false');
      }
    });

    navMobile.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navMobile.classList.remove('open', 'show');
        menuToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* Back to top button */
  const backTop = document.querySelector('.fab-top');
  if (backTop) {
    window.addEventListener('scroll', () => {
      backTop.classList.toggle('show', window.scrollY > 500);
    });
    backTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  /* Scroll reveal animation */
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach((el, i) => {
      el.style.transitionDelay = `${(i % 4) * 90}ms`;
      io.observe(el);
    });
  } else {
    revealEls.forEach(el => el.classList.add('in'));
  }

  /* Counter animation */
  const counters = document.querySelectorAll('[data-counter]');
  if ('IntersectionObserver' in window && counters.length) {
    const counterIO = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const target = parseInt(el.getAttribute('data-counter'), 10);
        const suffix = el.getAttribute('data-suffix') || '';
        const duration = 1600;
        const start = performance.now();
        function tick(now) {
          const progress = Math.min((now - start) / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 3);
          el.textContent = Math.round(eased * target).toLocaleString('en-IN') + suffix;
          if (progress < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
        counterIO.unobserve(el);
      });
    }, { threshold: 0.5 });
    counters.forEach(el => counterIO.observe(el));
  }

  /* Search box property-type toggle */
  document.querySelectorAll('.search-toggle button').forEach(btn => {
    btn.addEventListener('click', () => {
      btn.parentElement.querySelectorAll('button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });

  /* Filter chips */
  document.querySelectorAll('.filter-chip').forEach(chip => {
    chip.addEventListener('click', () => chip.classList.toggle('active'));
  });

  /* Property gallery thumb-swap */
  document.querySelectorAll('[data-gallery-thumb]').forEach(thumb => {
    thumb.addEventListener('click', () => {
      const mainImg = document.querySelector('[data-gallery-main]');
      const group = thumb.closest('[data-gallery]');
      if (!mainImg || !group) return;
      group.querySelectorAll('[data-gallery-thumb]').forEach(t => t.classList.remove('active-thumb'));
      thumb.classList.add('active-thumb');
      mainImg.querySelector('.img-ph-inner strong').textContent = thumb.getAttribute('data-label') || 'Property Image';
    });
  });

  /* Loan EMI calculator */
  const emiForm = document.querySelector('#emi-calculator');
  if (emiForm) {
    const calcEMI = () => {
      const amount = parseFloat(emiForm.querySelector('#loan-amount').value) || 0;
      const rate = parseFloat(emiForm.querySelector('#loan-rate').value) || 0;
      const years = parseFloat(emiForm.querySelector('#loan-years').value) || 0;
      const r = rate / 12 / 100;
      const n = years * 12;
      const result = document.querySelector('#emi-result');
      if (r === 0 || n === 0) { result.textContent = '₹ 0'; return; }
      const emi = (amount * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
      result.textContent = '₹ ' + Math.round(emi).toLocaleString('en-IN') + ' / month';
    };
    emiForm.querySelectorAll('input').forEach(inp => inp.addEventListener('input', calcEMI));
    calcEMI();
  }

  /* FAQ Accordion - only one open at a time */
  document.querySelectorAll('.faq-item').forEach(item => {
    item.addEventListener('toggle', () => {
      if (item.open) {
        document.querySelectorAll('.faq-item').forEach(other => {
          if (other !== item) other.removeAttribute('open');
        });
      }
    });
  });

  /* Testimonial slider */
  const slider = document.querySelector('[data-testi-slider]');
  if (slider) {
    let idx = 0;
    const track = slider.querySelector('.testi-slider-track');
    const cards = slider.querySelectorAll('.testi-card');
    const next = slider.querySelector('.testi-next');
    const prev = slider.querySelector('.testi-prev');
    const go = (i) => {
      idx = (i + cards.length) % cards.length;
      track.style.transform = `translateX(-${idx * 100}%)`;
    };
    if (next) next.addEventListener('click', () => go(idx + 1));
    if (prev) prev.addEventListener('click', () => go(idx - 1));
  }

  /* Reel Lightbox Modal */
  const reelModal = document.createElement('div');
  reelModal.className = 'reel-modal';
  reelModal.id = 'reel-lightbox-modal';
  reelModal.innerHTML = `
    <div class="reel-modal-content">
      <button class="reel-modal-close" aria-label="Close modal">&times;</button>
      <div class="reel-iframe-container" id="reel-container"></div>
    </div>
  `;
  document.body.appendChild(reelModal);

  const reelContainer = document.getElementById('reel-container');
  const modalClose = reelModal.querySelector('.reel-modal-close');

  const closeModal = () => {
    reelModal.classList.remove('active');
    reelContainer.innerHTML = '';
  };

  modalClose.addEventListener('click', closeModal);
  reelModal.addEventListener('click', (e) => {
    if (e.target === reelModal) closeModal();
  });

  document.querySelectorAll('[data-reel-url]').forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      const reelUrl = trigger.getAttribute('data-reel-url');
      if (!reelUrl) return;
      
      let embedUrl = reelUrl;
      if (!embedUrl.endsWith('/embed')) {
        embedUrl = embedUrl.replace(/\/$/, '') + '/embed';
      }

      reelContainer.innerHTML = `<iframe src="${embedUrl}" allowtransparency="true" allowfullscreen="true" frameborder="0" scrolling="no"></iframe>`;
      reelModal.classList.add('active');
    });
  });

  /* 3D Tilt Parallax on Hero Property Visual */
  const heroVisual = document.querySelector('.hero-visual');
  if (heroVisual) {
    heroVisual.addEventListener('mousemove', (e) => {
      const rect = heroVisual.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      heroVisual.style.transform = `perspective(1000px) rotateY(${x / 35}deg) rotateX(${-y / 35}deg)`;
    });
    heroVisual.addEventListener('mouseleave', () => {
      heroVisual.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg)';
      heroVisual.style.transition = 'transform 0.5s ease';
    });
  }

});


