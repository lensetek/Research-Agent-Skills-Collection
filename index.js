document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide Icons
  lucide.createIcons();

  // ==========================================================================
  // MOBILE MENU TOGGLE
  // ==========================================================================
  const menuToggle = document.getElementById('menu-toggle');
  const mobileNav = document.getElementById('mobile-nav');

  if (menuToggle && mobileNav) {
    menuToggle.addEventListener('click', () => {
      mobileNav.classList.toggle('active');
      const icon = menuToggle.querySelector('i');
      if (mobileNav.classList.contains('active')) {
        icon.setAttribute('data-lucide', 'x');
      } else {
        icon.setAttribute('data-lucide', 'menu');
      }
      lucide.createIcons();
    });

    // Close mobile nav when clicking a link
    mobileNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileNav.classList.remove('active');
        const icon = menuToggle.querySelector('i');
        icon.setAttribute('data-lucide', 'menu');
        lucide.createIcons();
      });
    });
  }

  // ==========================================================================
  // INTERACTIVE TABS (SKILLS EXPLORER)
  // ==========================================================================
  const tabButtons = document.querySelectorAll('.tab-btn');
  const tabPanels = document.querySelectorAll('.tab-panel');

  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      // Remove active from all buttons
      tabButtons.forEach(b => b.classList.remove('active'));
      // Add active to current button
      btn.classList.add('active');

      const targetPhase = btn.getAttribute('data-phase');

      // Hide all panels and remove active state
      tabPanels.forEach(panel => {
        panel.classList.remove('active');
      });

      // Show target panel with a slight delay for transition
      const targetPanel = document.getElementById(targetPhase);
      if (targetPanel) {
        targetPanel.classList.add('active');
      }
    });
  });

  // ==========================================================================
  // COPY TO CLIPBOARD UTILITY
  // ==========================================================================
  const copyBtn = document.getElementById('copy-btn');
  const promptCode = document.getElementById('prompt-code');

  if (copyBtn && promptCode) {
    copyBtn.addEventListener('click', () => {
      const textToCopy = promptCode.textContent;
      
      navigator.clipboard.writeText(textToCopy).then(() => {
        // Change button state to success
        copyBtn.classList.add('success');
        copyBtn.innerHTML = `<i data-lucide="check"></i> <span>Disalin!</span>`;
        lucide.createIcons();

        // Reset button state after 2 seconds
        setTimeout(() => {
          copyBtn.classList.remove('success');
          copyBtn.innerHTML = `<i data-lucide="copy"></i> <span>Salin</span>`;
          lucide.createIcons();
        }, 2000);
      }).catch(err => {
        console.error('Gagal menyalin teks: ', err);
      });
    });
  }

  // ==========================================================================
  // INTERSECTION OBSERVER FOR ENTRY ANIMATIONS
  // ==========================================================================
  const animatedElements = document.querySelectorAll('.animate-on-scroll');

  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        // Stop observing once animated
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  animatedElements.forEach(el => observer.observe(el));
});
