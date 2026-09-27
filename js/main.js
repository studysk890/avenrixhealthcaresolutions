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
   * 1. STICKY HEADER SCROLL STATE
   * Adds 'is-scrolled' class when scrolled past 50px.
   */
  let lastScrollY = window.scrollY;
  let ticking = false;

  function updateHeaderState() {
    const currentScrollY = window.scrollY;
    if (currentScrollY > 50) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }
    ticking = false;
  }

  window.addEventListener('scroll', function () {
    lastScrollY = window.scrollY;
    if (!ticking) {
      window.requestAnimationFrame(updateHeaderState);
      ticking = true;
    }
  }, { passive: true });

  // Initialize header state on page load
  updateHeaderState();

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

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });

        // Update active class on desktop nav
        document.querySelectorAll('.avx-header__nav-link').forEach(function (link) {
          link.classList.remove('is-active');
        });
        if (this.classList.contains('avx-header__nav-link')) {
          this.classList.add('is-active');
        }
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

      // Construct structured inquiry payload
      const inquiryPayload = {
        name: (nameInput.value || '').trim(),
        company: companyInput ? (companyInput.value || '').trim() || null : null,
        email: (emailInput.value || '').trim(),
        phone: (phoneInput.value || '').trim(),
        product: productSelect ? productSelect.value || null : null,
        message: messageInput ? (messageInput.value || '').trim() || null : null,
        submittedAt: new Date().toISOString()
      };

      // ======================================================================
      // BACKEND INTEGRATION POINT:
      // The form does not submit to a fictional endpoint or third-party service.
      // Hook your production backend API endpoint / webhook / fetch here:
      // e.g.:
      // const response = await fetch('/api/avenrix-inquiries', {
      //   method: 'POST',
      //   headers: { 'Content-Type': 'application/json' },
      //   body: JSON.stringify(inquiryPayload)
      // });
      // ======================================================================

      // Transition smoothly from form to success confirmation state
      form.classList.add('is-hidden');
      successBlock.classList.add('is-visible');
      successBlock.setAttribute('tabindex', '-1');
      successBlock.focus();
    });

    // Reset button handler: return to clean form
    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        form.reset();
        clearFieldError(nameWrap, nameInput, nameError);
        clearFieldError(emailWrap, emailInput, emailError);
        clearFieldError(phoneWrap, phoneInput, phoneError);

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

})();

