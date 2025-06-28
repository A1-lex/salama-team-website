document.addEventListener('DOMContentLoaded', () => {

  // — Smooth Scrolling for Anchor Links —
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  const typedTarget = document.getElementById('typed-text');
  if (typedTarget) {
    new Typed('#typed-text', {
      strings: [
        "AI-Powered Cybersecurity for Safer Education & Government Institutions",
        "Detecting Phishing & Threats in Real-Time",
        "Protecting Kenya’s Digital Future"
      ],
      typeSpeed: 50,
      backSpeed: 30,
      backDelay: 2000,
      loop: true
    });
  }


  // — Back to Top Button —
  const backBtn = document.getElementById('btn-back-to-top');
  if (backBtn) {
    window.addEventListener('scroll', () => {
      backBtn.style.display = window.scrollY > 300 ? 'block' : 'none';
    });
    backBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // — Dark Mode Toggle —
  const dmSwitch = document.getElementById('darkModeSwitch');
  if (dmSwitch) {
    if (localStorage.getItem('dark-mode') === 'enabled') {
      document.body.classList.add('dark-mode');
      dmSwitch.checked = true;
    }
    dmSwitch.addEventListener('change', function () {
      if (this.checked) {
        document.body.classList.add('dark-mode');
        localStorage.setItem('dark-mode', 'enabled');
      } else {
        document.body.classList.remove('dark-mode');
        localStorage.setItem('dark-mode', 'disabled');
      }
    });
  }

  // — Page Loader —
  const loader = document.getElementById('loader-wrapper');
  if (loader) {
    window.addEventListener('load', () => {
      loader.classList.add('fade-out');
    });
  }

  // — Stats Counter Animation —
  const counters = document.querySelectorAll('.counter');
  const speed = 200; // lower is faster

  counters.forEach(counter => {
    const animate = () => {
      const value = +counter.getAttribute('data-target');
      const data = +counter.innerText;
      const increment = value / speed;

      if (data < value) {
        counter.innerText = Math.ceil(data + increment);
        setTimeout(animate, 30);
      } else {
        counter.innerText = value;
      }
    };

    const observer = new IntersectionObserver(entries => {
      if (entries[0].isIntersecting) {
        animate();
        observer.disconnect();
      }
    }, { threshold: 0.5 });

    observer.observe(counter);
  });

  // — Logo Animation on Scroll —
  const logo = document.querySelector('.logo-animate');
  if (logo) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          logo.classList.add('visible');
        }
      });
    }, { threshold: 0.5 });
    observer.observe(logo);
  }

});
