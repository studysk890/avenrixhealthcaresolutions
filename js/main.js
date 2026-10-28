/**
 * AVENRIX HEALTHCARE SOLUTIONS — MAIN JAVASCRIPT
 * Modular UI Controller: Sticky Header, Mobile Drawer, Smooth Nav, Back-to-Top
 */

(function () {
  'use strict';

  // DOM Elements
  const header = document.getElementById('header');
  const menuToggle = document.getElementById('menuToggle');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const drawerBackdrop = document.getElementById('drawerBackdrop');
  const navLinks = document.querySelectorAll('.avx-header__nav-link, .avx-drawer__link');
  const backToTopBtn = document.getElementById('backToTop');

  /**
   * 1. STICKY HEADER & ACTIVE SCROLL-SPY NAVIGATION
   * Adds 'is-scrolled' class when scrolled past 50px.
   * Continuously monitors scroll position and updates '.is-active' on both
   * desktop (.avx-header__nav-link) and mobile drawer (.avx-drawer__link)
   * to accurately reflect whichever section is currently showing.
   */
  const sections = ['home', 'about', 'products', 'values', 'contact']
    .map(id => ({ id, el: document.getElementById(id) }))
    .filter(s => s.el !== null);

  const desktopNavLinks = document.querySelectorAll('.avx-header__nav-link');
  const drawerNavLinks = document.querySelectorAll('.avx-drawer__link');

  let currentActiveId = null;

  function setActiveNavLink(activeId) {
    if (!activeId || currentActiveId === activeId) return;
    currentActiveId = activeId;

    desktopNavLinks.forEach(link => {
      const href = link.getAttribute('href');
      const isMatch = href === '#' + activeId;
      link.classList.toggle('is-active', isMatch);
      if (isMatch) {
        link.setAttribute('aria-current', 'page');
      } else {
        link.removeAttribute('aria-current');
      }
    });

    drawerNavLinks.forEach(link => {
      const href = link.getAttribute('href');
      const isMatch = href === '#' + activeId;
      link.classList.toggle('is-active', isMatch);
      if (isMatch) {
        link.setAttribute('aria-current', 'page');
      } else {
        link.removeAttribute('aria-current');
      }
    });
  }

  function updateActiveSectionOnScroll() {
    const scrollY = window.scrollY;
    const windowHeight = window.innerHeight;
    const docHeight = document.documentElement.scrollHeight;
    const headerHeight = header ? header.offsetHeight : 80;

    // 1. Bottom of page reached -> activate the last section ('contact')
    if (windowHeight + scrollY >= docHeight - 60) {
      setActiveNavLink('contact');
      return;
    }

    // 2. Near top of page -> activate 'home'
    if (scrollY < 120) {
      setActiveNavLink('home');
      return;
    }

    // 3. Dynamic checkpoint: header offset + 25% of viewport
    const checkpoint = scrollY + headerHeight + (windowHeight * 0.25);

    let activeId = 'home';
    for (let i = 0; i < sections.length; i++) {
      const sec = sections[i];
      const secTop = sec.el.getBoundingClientRect().top + scrollY;
      if (checkpoint >= secTop) {
        activeId = sec.id;
      } else {
        break;
      }
    }

    setActiveNavLink(activeId);
  }

  let lastScrollY = window.scrollY;
  let ticking = false;

  function onScrollTick() {
    const currentScrollY = window.scrollY;

    // Sticky Header Class
    if (currentScrollY > 50) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }

    // Active Section ScrollSpy
    updateActiveSectionOnScroll();

    ticking = false;
  }

  window.addEventListener('scroll', function () {
    lastScrollY = window.scrollY;
    if (!ticking) {
      window.requestAnimationFrame(onScrollTick);
      ticking = true;
    }
  }, { passive: true });

  // Initialize on page load and window resize
  onScrollTick();
  window.addEventListener('resize', function () {
    if (!ticking) {
      window.requestAnimationFrame(onScrollTick);
      ticking = true;
    }
  }, { passive: true });

  /**
   * 2. ACCESSIBLE MOBILE DRAWER NAVIGATION
   */
  function openDrawer() {
    menuToggle.setAttribute('aria-expanded', 'true');
    menuToggle.setAttribute('aria-label', 'Close Navigation Menu');
    mobileDrawer.classList.add('is-open');
    mobileDrawer.setAttribute('aria-hidden', 'false');
    drawerBackdrop.classList.add('is-open');
    drawerBackdrop.setAttribute('aria-hidden', 'false');
    document.body.classList.add('avx-scroll-locked');

    // Focus close button or first link inside drawer
    const drawerCloseBtn = document.getElementById('drawerClose');
    if (drawerCloseBtn) {
      setTimeout(() => drawerCloseBtn.focus(), 150);
    } else {
      const firstLink = mobileDrawer.querySelector('.avx-drawer__link');
      if (firstLink) {
        setTimeout(() => firstLink.focus(), 150);
      }
    }
  }

  function closeDrawer() {
    menuToggle.setAttribute('aria-expanded', 'false');
    menuToggle.setAttribute('aria-label', 'Open Navigation Menu');
    mobileDrawer.classList.remove('is-open');
    mobileDrawer.setAttribute('aria-hidden', 'true');
    drawerBackdrop.classList.remove('is-open');
    drawerBackdrop.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('avx-scroll-locked');
    menuToggle.focus();
  }

  if (menuToggle && mobileDrawer && drawerBackdrop) {
    menuToggle.addEventListener('click', function (e) {
      e.preventDefault();
      const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
      if (isExpanded) {
        closeDrawer();
      } else {
        openDrawer();
      }
    });

    // Close on explicit drawer close button click
    const drawerClose = document.getElementById('drawerClose');
    if (drawerClose) {
      drawerClose.addEventListener('click', function (e) {
        e.preventDefault();
        closeDrawer();
      });
    }

    // Close on backdrop click
    drawerBackdrop.addEventListener('click', closeDrawer);

    // Close on Escape key press
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && (menuToggle.getAttribute('aria-expanded') === 'true' || mobileDrawer.classList.contains('is-open'))) {
        closeDrawer();
      }
    });

    // Close on link click
    mobileDrawer.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        closeDrawer();
      });
    });
  }

  /**
   * 3. SMOOTH NAVIGATION WITH FIXED HEADER OFFSET
   */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || !targetId) return;

      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        const headerHeight = header ? header.offsetHeight : 0;
        const targetPosition = targetEl.getBoundingClientRect().top + window.pageYOffset - headerHeight;

        // Immediately set active nav link for responsive feedback
        const cleanId = targetId.replace(/^#/, '');
        if (cleanId) {
          setActiveNavLink(cleanId);
        }

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  /**
   * 4. BACK TO TOP INTERACTION
   */
  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', function (e) {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  /**
   * 5. CONTACT FORM VALIDATION & SUBMISSION
   * High-contrast split-screen inquiry form with client-side validation,
   * accessible ARIA state management, and structured console payload.
   */
  function initContactForm() {
    // ========================================================================
    // GOOGLE SHEETS INTEGRATION ENDPOINT:
    // Deployed Webhook URL (Obfuscated to prevent automated crawler harvesting)
    // ========================================================================
    const GOOGLE_SHEETS_SCRIPT_URL = typeof atob === 'function' 
      ? atob('aHR0cHM6Ly9zY3JpcHQuZ29vZ2xlLmNvbS9tYWNyb3Mvcy9BS2Z5Y2J5aFZHNG9scFhsYVpDcVFOdHl4N3MtOERXMXUxR0syT2wzT3FYVDlsc0c4eHBidFNmOFVxTTBTWVBTOVRWamRTVHQvZXhlYw==')
      : 'https://script.google.com/macros/s/AKfycbyhVG4olpXlaZCqQNtyx7s-8DW1u1GK2Ol3OqXT9lsG8xpbtSf8UqM0SYPS9TVjdSTt/exec';

    const form = document.getElementById('avxContactForm');
    const successBlock = document.getElementById('avxContactSuccess');
    const resetBtn = document.getElementById('avxContactReset');

    if (!form || !successBlock) return;

    // Field references
    const nameInput = document.getElementById('avxContactName');
    const nameWrap = document.getElementById('fieldWrapName');
    const nameError = document.getElementById('avxNameError');

    const companyInput = document.getElementById('avxContactCompany');

    const emailInput = document.getElementById('avxContactEmail');
    const emailWrap = document.getElementById('fieldWrapEmail');
    const emailError = document.getElementById('avxEmailError');

    const phoneInput = document.getElementById('avxContactPhone');
    const phoneWrap = document.getElementById('fieldWrapPhone');
    const phoneError = document.getElementById('avxPhoneError');

    const productSelect = document.getElementById('avxContactProduct');
    const messageInput = document.getElementById('avxContactMessage');

    const submitBtn = document.getElementById('avxContactSubmit');
    const submitText = submitBtn ? submitBtn.querySelector('.avx-contact__submit-text') : null;
    const submitArrow = submitBtn ? submitBtn.querySelector('.avx-contact__arrow') : null;
    const alertBox = document.getElementById('avxContactAlert');

    // Validation patterns
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
    // Allows international formats: +..., spaces, hyphens, parentheses, minimum 7 digits
    const phoneCharRegex = /^[0-9+\s\-()]{7,25}$/;

    function setFieldError(wrap, input, errorEl, message) {
      if (!wrap || !input || !errorEl) return;
      wrap.classList.add('has-error');
      input.setAttribute('aria-invalid', 'true');
      errorEl.textContent = message;
    }

    function clearFieldError(wrap, input, errorEl) {
      if (!wrap || !input || !errorEl) return;
      wrap.classList.remove('has-error');
      input.removeAttribute('aria-invalid');
      errorEl.textContent = '';
    }

    function setSubmittingState(isSubmitting) {
      if (!submitBtn) return;
      submitBtn.disabled = isSubmitting;
      submitBtn.classList.toggle('is-submitting', isSubmitting);

      if (isSubmitting) {
        if (submitText) submitText.textContent = 'Sending Inquiry...';
        if (submitArrow) submitArrow.style.display = 'none';
        if (!submitBtn.querySelector('.avx-contact__spinner')) {
          const spinner = document.createElement('span');
          spinner.className = 'avx-contact__spinner';
          spinner.setAttribute('aria-hidden', 'true');
          submitBtn.prepend(spinner);
        }
      } else {
        if (submitText) submitText.textContent = 'Submit Inquiry';
        if (submitArrow) submitArrow.style.display = '';
        const spinner = submitBtn.querySelector('.avx-contact__spinner');
        if (spinner) spinner.remove();
      }
    }

    function showFormAlert(message) {
      if (!alertBox) return;
      alertBox.textContent = message;
      alertBox.classList.add('is-visible');
    }

    function clearFormAlert() {
      if (!alertBox) return;
      alertBox.textContent = '';
      alertBox.classList.remove('is-visible');
    }

    function validateName() {
      const val = (nameInput.value || '').trim();
      if (!val) {
        setFieldError(nameWrap, nameInput, nameError, 'Please enter your full name.');
        return false;
      }
      if (val.length < 2) {
        setFieldError(nameWrap, nameInput, nameError, 'Full name must be at least 2 characters.');
        return false;
      }
      clearFieldError(nameWrap, nameInput, nameError);
      return true;
    }

    function validateEmail() {
      const val = (emailInput.value || '').trim();
      if (!val) {
        setFieldError(emailWrap, emailInput, emailError, 'Please enter your email address.');
        return false;
      }
      if (!emailRegex.test(val)) {
        setFieldError(emailWrap, emailInput, emailError, 'Please enter a valid email address (e.g. name@organization.com).');
        return false;
      }
      clearFieldError(emailWrap, emailInput, emailError);
      return true;
    }

    function validatePhone() {
      const val = (phoneInput.value || '').trim();
      if (!val) {
        setFieldError(phoneWrap, phoneInput, phoneError, 'Please enter your phone number.');
        return false;
      }
      const digitsOnly = val.replace(/\D/g, '');
      if (!phoneCharRegex.test(val) || digitsOnly.length < 7) {
        setFieldError(phoneWrap, phoneInput, phoneError, 'Please enter a valid phone number (at least 7 digits).');
        return false;
      }
      clearFieldError(phoneWrap, phoneInput, phoneError);
      return true;
    }

    // Real-time validation listeners on blur and input
    if (nameInput) {
      nameInput.addEventListener('blur', validateName);
      nameInput.addEventListener('input', function () {
        if (nameWrap && nameWrap.classList.contains('has-error')) validateName();
      });
    }

    if (emailInput) {
      emailInput.addEventListener('blur', validateEmail);
      emailInput.addEventListener('input', function () {
        if (emailWrap && emailWrap.classList.contains('has-error')) validateEmail();
      });
    }

    if (phoneInput) {
      phoneInput.addEventListener('blur', validatePhone);
      phoneInput.addEventListener('input', function () {
        if (phoneWrap && phoneWrap.classList.contains('has-error')) validatePhone();
      });
    }

    // Form submission handler
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      const isNameValid = validateName();
      const isEmailValid = validateEmail();
      const isPhoneValid = validatePhone();

      if (!isNameValid || !isEmailValid || !isPhoneValid) {
        // Focus the first invalid element
        if (!isNameValid && nameInput) {
          nameInput.focus();
        } else if (!isEmailValid && emailInput) {
          emailInput.focus();
        } else if (!isPhoneValid && phoneInput) {
          phoneInput.focus();
        }
        return;
      }

      if (submitBtn && submitBtn.disabled) return;

      clearFormAlert();
      setSubmittingState(true);

      // Construct structured inquiry payload
      const inquiryPayload = {
        name: (nameInput.value || '').trim(),
        company: companyInput ? (companyInput.value || '').trim() || null : null,
        email: (emailInput.value || '').trim(),
        phone: (phoneInput.value || '').trim(),
        product: productSelect ? productSelect.value || null : null,
        message: messageInput ? (messageInput.value || '').trim() || null : null,
        submittedAt: new Date().toLocaleString()
      };

      function handleSuccess() {
        setSubmittingState(false);
        form.classList.add('is-hidden');
        successBlock.classList.add('is-visible');
        successBlock.setAttribute('tabindex', '-1');
        successBlock.focus();
      }

      // If Google Sheets endpoint is configured, POST to it
      if (GOOGLE_SHEETS_SCRIPT_URL && GOOGLE_SHEETS_SCRIPT_URL.trim() !== '') {
        // Send as text/plain with no-cors to prevent preflight OPTIONS failures on Google Apps Script
        fetch(GOOGLE_SHEETS_SCRIPT_URL, {
          method: 'POST',
          mode: 'no-cors',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8'
          },
          body: JSON.stringify(inquiryPayload)
        })
        .then(() => {
          handleSuccess();
        })
        .catch((error) => {
          console.error('[Avenrix Contact Form] Google Sheets submission error:', error);
          setSubmittingState(false);
          showFormAlert('We could not send your inquiry due to a network connection issue. Please check your connection or email us directly.');
        });
      } else {
        // Fallback for local preview when endpoint URL is pending deployment
        console.info('[Avenrix Contact Form] Google Sheets URL not configured yet. Logged payload:', inquiryPayload);
        setTimeout(() => {
          handleSuccess();
        }, 500);
      }
    });

    // Reset button handler: return to clean form
    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        form.reset();
        clearFieldError(nameWrap, nameInput, nameError);
        clearFieldError(emailWrap, emailInput, emailError);
        clearFieldError(phoneWrap, phoneInput, phoneError);
        clearFormAlert();
        setSubmittingState(false);

        successBlock.classList.remove('is-visible');
        form.classList.remove('is-hidden');

        if (nameInput) {
          nameInput.focus();
        }
      });
    }
  }

  // Initialize Contact Form
  initContactForm();

  /**
   * 6. AHU & HVAC DUAL-IMAGE AUTO SLIDER (Card 01)
   * Automatically cycles every 3 seconds in an infinite loop.
   * Pauses on hover, focus, and tab switch.
   * Supports manual dot controls and mobile touch swipe.
   */
  function initAhuHvacSlider() {
    const slider = document.getElementById('ahuHvacSlider');
    if (!slider) return;

    const slides = slider.querySelectorAll('.avx-slider-slide');
    const dots = slider.querySelectorAll('.avx-slider-dot');
    if (slides.length < 2) return;

    const badge = document.getElementById('ahuHvacBadge');
    const badgeSlides = badge ? badge.querySelectorAll('.avx-badge-slide') : [];

    let currentIndex = 0;
    let isTransitioning = false;
    let timer = null;
    const INTERVAL = 3000; // 3 seconds
    const TRANSITION_MS = 650; // CSS animation duration

    function updateDots(activeIdx) {
      dots.forEach((dot, idx) => {
        const isActive = idx === activeIdx;
        dot.classList.toggle('is-active', isActive);
        dot.setAttribute('aria-selected', isActive ? 'true' : 'false');
      });
    }

    function goToSlide(nextIndex, direction = 'next') {
      if (isTransitioning || nextIndex === currentIndex) return;
      isTransitioning = true;

      const currentSlide = slides[currentIndex];
      const nextSlide = slides[nextIndex];

      const currentBadge = badgeSlides[currentIndex];
      const nextBadge = badgeSlides[nextIndex];

      // Prepare incoming slide and badge text position without transition
      nextSlide.style.transition = 'none';
      nextSlide.style.transform = direction === 'next' ? 'translateX(100%)' : 'translateX(-100%)';
      nextSlide.classList.add('is-animating');

      if (nextBadge) {
        nextBadge.style.transition = 'none';
        nextBadge.style.transform = direction === 'next' ? 'translateX(100%)' : 'translateX(-100%)';
        nextBadge.style.opacity = '0';
        nextBadge.classList.add('is-animating');
      }

      // Force layout reflow
      void nextSlide.offsetWidth;
      if (nextBadge) void nextBadge.offsetWidth;

      // Animate both slides and badge text
      const transitionStyle = 'transform 0.65s cubic-bezier(0.25, 1, 0.5, 1)';
      const badgeTransition = 'transform 0.65s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.45s ease';

      currentSlide.style.transition = transitionStyle;
      nextSlide.style.transition = transitionStyle;

      currentSlide.style.transform = direction === 'next' ? 'translateX(-100%)' : 'translateX(100%)';
      nextSlide.style.transform = 'translateX(0)';

      if (currentBadge && nextBadge) {
        currentBadge.style.transition = badgeTransition;
        nextBadge.style.transition = badgeTransition;

        currentBadge.style.transform = direction === 'next' ? 'translateX(-100%)' : 'translateX(100%)';
        currentBadge.style.opacity = '0';
        nextBadge.style.transform = 'translateX(0)';
        nextBadge.style.opacity = '1';
      }

      updateDots(nextIndex);

      setTimeout(() => {
        currentSlide.classList.remove('is-active', 'is-animating');
        currentSlide.style.transition = 'none';
        currentSlide.style.transform = '';

        nextSlide.classList.add('is-active');
        nextSlide.classList.remove('is-animating');
        nextSlide.style.transition = '';
        nextSlide.style.transform = '';

        if (currentBadge && nextBadge) {
          currentBadge.classList.remove('is-active', 'is-animating');
          currentBadge.style.transition = 'none';
          currentBadge.style.transform = '';
          currentBadge.style.opacity = '';

          nextBadge.classList.add('is-active');
          nextBadge.classList.remove('is-animating');
          nextBadge.style.transition = '';
          nextBadge.style.transform = '';
          nextBadge.style.opacity = '';

          if (badge) {
            badge.setAttribute('aria-label', 'Current System: ' + (nextBadge.textContent || '').trim());
          }
        }

        currentIndex = nextIndex;
        isTransitioning = false;
      }, TRANSITION_MS);
    }

    function nextSlide() {
      const nextIndex = (currentIndex + 1) % slides.length;
      goToSlide(nextIndex, 'next');
    }

    function prevSlide() {
      const prevIndex = (currentIndex - 1 + slides.length) % slides.length;
      goToSlide(prevIndex, 'prev');
    }

    function startAutoPlay() {
      stopAutoPlay();
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      timer = setInterval(nextSlide, INTERVAL);
    }

    function stopAutoPlay() {
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
    }

    // Dot navigation
    dots.forEach(dot => {
      dot.addEventListener('click', function (e) {
        e.preventDefault();
        const targetIdx = parseInt(dot.getAttribute('data-slide'), 10);
        if (targetIdx !== currentIndex) {
          goToSlide(targetIdx, targetIdx > currentIndex ? 'next' : 'prev');
          startAutoPlay();
        }
      });
    });

    // Pause on user hover and focus (WCAG compliance)
    const card = slider.closest('.avx-product-card') || slider;
    card.addEventListener('mouseenter', stopAutoPlay);
    card.addEventListener('mouseleave', startAutoPlay);
    card.addEventListener('focusin', stopAutoPlay);
    card.addEventListener('focusout', startAutoPlay);

    // Pause when page tab is hidden
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) {
        stopAutoPlay();
      } else {
        startAutoPlay();
      }
    });

    // Touch swipe support for mobile
    let touchStartX = 0;
    slider.addEventListener('touchstart', function (e) {
      touchStartX = e.changedTouches[0].screenX;
      stopAutoPlay();
    }, { passive: true });

    slider.addEventListener('touchend', function (e) {
      const touchEndX = e.changedTouches[0].screenX;
      const diffX = touchEndX - touchStartX;
      if (Math.abs(diffX) > 40) {
        if (diffX < 0) {
          nextSlide();
        } else {
          prevSlide();
        }
      }
      startAutoPlay();
    }, { passive: true });

    // Initial state
    slides.forEach((slide, idx) => {
      slide.classList.toggle('is-active', idx === 0);
    });
    if (badgeSlides.length > 0) {
      badgeSlides.forEach((bSlide, idx) => {
        bSlide.classList.toggle('is-active', idx === 0);
      });
      if (badge) {
        badge.setAttribute('aria-label', 'Current System: ' + (badgeSlides[0].textContent || '').trim());
      }
    }
    updateDots(0);

    // Start 3-second infinite auto loop
    startAutoPlay();
  }

  // Initialize AHU & HVAC Slider
  initAhuHvacSlider();

  /**
   * 7. SOURCE PROTECTION & ANTI-CLONING SHIELD
   * Prevents right-click context menu, source-viewing shortcuts,
   * page saving shortcuts, and image dragging.
   */
  function initAntiCloningShield() {
    // Disable right-click context menu
    document.addEventListener('contextmenu', function (e) {
      e.preventDefault();
      return false;
    });

    // Disable keyboard shortcuts for viewing source, saving, and inspecting
    document.addEventListener('keydown', function (e) {
      const isCtrlOrMeta = e.ctrlKey || e.metaKey;
      const key = (e.key || '').toLowerCase();

      // Ctrl/Cmd + U (View Source)
      // Ctrl/Cmd + S (Save Webpage)
      // Ctrl/Cmd + P (Print / Save PDF)
      // F12 or Ctrl/Cmd + Shift + I/J/C (Developer Tools / Inspect)
      if (
        (isCtrlOrMeta && (key === 'u' || key === 's' || key === 'p')) ||
        (isCtrlOrMeta && e.shiftKey && (key === 'i' || key === 'j' || key === 'c')) ||
        e.key === 'F12'
      ) {
        e.preventDefault();
        e.stopPropagation();
        return false;
      }
    });

    // Disable image dragging to prevent asset ripping
    document.addEventListener('dragstart', function (e) {
      if (e.target && e.target.nodeName === 'IMG') {
        e.preventDefault();
        return false;
      }
    });
  }

  // Initialize Anti-Cloning Shield
  initAntiCloningShield();

})();


