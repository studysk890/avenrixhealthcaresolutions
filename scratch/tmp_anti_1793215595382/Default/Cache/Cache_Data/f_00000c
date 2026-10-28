/**
 * AVENRIX HEALTHCARE SOLUTIONS — PHASE 6 MOTION & INTERACTION CONTROLLER
 * Full-page Architectural GSAP / ScrollTrigger Engine
 * 
 * Modular Controllers:
 *  - initHeaderAnimations()
 *  - initHeroAnimations()
 *  - initAboutAnimations()
 *  - initProductAnimations()
 *  - initValuesAnimations()
 *  - initContactAnimations()
 *  - initFooterAnimations()
 * 
 * Architectural Characteristics:
 *  - Precision, restraint, deceleration (power2.out, power3.out, expo.out)
 *  - No elastic, bounce, or gratuitous 3D transforms
 *  - Responsive adaptation across Desktop, Tablet, and Mobile
 *  - Strict prefers-reduced-motion compliance
 *  - Orientation change & debounced font-load refresh handlers
 */

(function () {
  'use strict';

  // ---------------------------------------------------------------------------
  // Global Architectural Motion Design Tokens
  // ---------------------------------------------------------------------------
  const MOTION = {
    duration: {
      fast: 0.3,       // 0.25 - 0.35s: Micro-interactions & subtle shifts
      medium: 0.55,    // 0.50 - 0.70s: Standard layout transitions
      reveal: 0.8,     // 0.70 - 1.00s: Major structural reveals
      editorial: 1.05  // 0.90 - 1.20s: Monumental text & image sequences
    },
    ease: {
      decel: 'power2.out',       // Crisp architectural stop
      editorial: 'power3.out',   // Smooth editorial deceleration
      cinematic: 'expo.out',     // High-velocity settling curve
      inOut: 'power3.inOut'      // Controlled geometric reveal
    },
    distance: {
      sm: 12,
      md: 20,
      lg: 32
    }
  };

  // Wait for DOM to be ready
  document.addEventListener('DOMContentLoaded', initAvenrixAnimations);

  /**
   * Main Orchestrator
   */
  function initAvenrixAnimations() {
    // Check for GSAP availability
    if (typeof gsap === 'undefined') {
      console.warn('[Avenrix Motion] GSAP is not loaded. Falling back to native CSS layout.');
      return;
    }

    // Register ScrollTrigger if loaded
    if (typeof ScrollTrigger !== 'undefined') {
      gsap.registerPlugin(ScrollTrigger);
    }

    // Check prefers-reduced-motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) {
      applyReducedMotionState();
      return;
    }

    // Initialize individual section controllers
    initHeaderAnimations();
    initHeroAnimations();
    initAboutAnimations();
    initProductAnimations();
    initValuesAnimations();
    initContactAnimations();
    initFooterAnimations();

    // Register global resize and orientation safety listeners
    initSafetyHandlers();
  }

  /**
   * Reduced Motion Fallback: Instantly resolves all elements to final visible layout
   */
  function applyReducedMotionState() {
    const allAnimatedElements = [
      '.avx-header',
      '.avx-hero__visual',
      '.avx-hero__eyebrow',
      '.avx-hero__title',
      '.avx-hero__desc',
      '.avx-hero__ctas > *',
      '.avx-about__meta',
      '.avx-about__title',
      '.avx-about__intro',
      '.avx-about__accent-rule',
      '.avx-about__narrative > *',
      '.avx-about__media',
      '.avx-about__image',
      '.avx-products__meta',
      '.avx-products__title',
      '.avx-products__intro',
      '.avx-products__accent-rule',
      '.avx-product-card',
      '.avx-values__meta',
      '.avx-values__title',
      '.avx-values__intro',
      '.avx-values__accent-rule',
      '.avx-values__manifesto',
      '.avx-value',
      '.avx-value__badge',
      '.avx-value__connector',
      '.avx-contact__aside-inner > *',
      '.avx-contact__accent-rule',
      '.avx-contact__aside-grid',
      '.avx-contact__panel-inner',
      '.avx-contact__field',
      '.avx-contact__submit-wrap',
      '.avx-footer__pre-inner > *',
      '.avx-footer__grid > div',
      '.avx-footer__bottom'
    ];

    gsap.set(allAnimatedElements, {
      opacity: 1,
      x: 0,
      y: 0,
      scale: 1,
      clipPath: 'none',
      clearProps: 'all'
    });
  }

  /**
   * 1. HEADER ENTRANCE ANIMATION
   */
  function initHeaderAnimations() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    gsap.from('.avx-header', {
      y: -14,
      opacity: 0,
      duration: MOTION.duration.medium,
      ease: MOTION.ease.decel,
      clearProps: 'transform,opacity'
    });
  }

  /**
   * 2. HERO ENTRANCE SEQUENCE & SCROLL PARALLAX
   * Load Sequence:
   *  Header -> Hero Visual (scale 1.03 -> 1) -> Eyebrow -> Headline -> Description -> CTAs
   *  Both CTAs finish within 0.9s and have clearProps applied immediately.
   */
  function initHeroAnimations() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const heroTL = gsap.timeline({
      defaults: { ease: MOTION.ease.decel }
    });

    heroTL
      // Visual enters early with gentle settling scale
      .from('.avx-hero__visual', {
        opacity: 0,
        y: 16,
        scale: 1.03,
        duration: 0.6,
        ease: MOTION.ease.editorial,
        clearProps: 'transform,opacity'
      }, 0.05)
      // Editorial typography hierarchy
      .from('.avx-hero__eyebrow', {
        opacity: 0,
        y: 12,
        duration: 0.35,
        ease: MOTION.ease.decel,
        clearProps: 'transform,opacity'
      }, 0.15)
      .from('.avx-hero__title', {
        opacity: 0,
        y: 16,
        duration: 0.45,
        ease: MOTION.ease.editorial,
        clearProps: 'transform,opacity'
      }, 0.22)
      .from('.avx-hero__desc', {
        opacity: 0,
        y: 14,
        duration: 0.4,
        ease: MOTION.ease.decel,
        clearProps: 'transform,opacity'
      }, 0.32)
      // Primary & Secondary CTAs finish well within 0.9s
      .from('.avx-hero__ctas > *', {
        opacity: 0,
        y: 12,
        duration: 0.35,
        stagger: 0.08,
        ease: MOTION.ease.decel,
        clearProps: 'transform,opacity'
      }, 0.42);

    // Restrained Hero Scroll Parallax (Desktop Only ≥ 992px)
    if (typeof ScrollTrigger !== 'undefined') {
      const mm = gsap.matchMedia();
      mm.add('(min-width: 992px)', () => {
        gsap.to('.avx-hero__visual', {
          yPercent: 6,
          ease: 'none',
          scrollTrigger: {
            trigger: '.avx-hero',
            start: 'top top',
            end: 'bottom top',
            scrub: 1.2
          }
        });
      });
    }
  }

  /**
   * 3. ABOUT US EDITORIAL REVEAL & PARALLAX
   * Desktop: Staggered narrative reveal, architectural clip-path image entrance, subtle parallax scrub
   * Tablet/Mobile: Simple, clean vertical entrance
   */
  function initAboutAnimations() {
    const aboutSection = document.querySelector('.avx-about');
    if (!aboutSection || typeof ScrollTrigger === 'undefined') return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const mm = gsap.matchMedia();

    // Desktop (≥ 992px): Editorial clip-path reveal + subtle scroll parallax
    mm.add('(min-width: 992px)', () => {
      const aboutTL = gsap.timeline({
        scrollTrigger: {
          trigger: '.avx-about',
          start: 'top 75%',
          toggleActions: 'play none none none'
        }
      });

      aboutTL
        .from(['.avx-about__meta', '.avx-about__title', '.avx-about__intro', '.avx-about__accent-rule'], {
          opacity: 0,
          y: MOTION.distance.md,
          duration: MOTION.duration.medium,
          stagger: 0.06,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        })
        .from('.avx-about__narrative > *', {
          opacity: 0,
          y: MOTION.distance.sm,
          duration: MOTION.duration.fast + 0.1,
          stagger: 0.06,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        }, '-=0.25')
        .from('.avx-about__media', {
          opacity: 0,
          clipPath: 'inset(0% 100% 0% 0%)',
          duration: MOTION.duration.reveal,
          ease: MOTION.ease.inOut,
          clearProps: 'clipPath,opacity'
        }, 0.1)
        .from('.avx-about__image', {
          scale: 1.04,
          duration: MOTION.duration.reveal + 0.1,
          ease: MOTION.ease.decel,
          clearProps: 'transform'
        }, 0.1);

      // Restrained Parallax Scrub on Media Column
      gsap.to('.avx-about__media', {
        yPercent: 6,
        ease: 'none',
        scrollTrigger: {
          trigger: '.avx-about',
          start: 'top bottom',
          end: 'bottom top',
          scrub: 1.2
        }
      });
    });

    // Tablet (640px – 991px)
    mm.add('(min-width: 640px) and (max-width: 991px)', () => {
      const aboutTL = gsap.timeline({
        scrollTrigger: {
          trigger: '.avx-about',
          start: 'top 80%',
          toggleActions: 'play none none none'
        }
      });

      aboutTL
        .from(['.avx-about__meta', '.avx-about__title', '.avx-about__intro', '.avx-about__accent-rule'], {
          opacity: 0,
          y: MOTION.distance.sm,
          duration: MOTION.duration.medium,
          stagger: 0.06,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        })
        .from('.avx-about__narrative > *', {
          opacity: 0,
          y: MOTION.distance.sm,
          duration: MOTION.duration.medium,
          stagger: 0.06,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        }, '-=0.25')
        .from('.avx-about__media', {
          opacity: 0,
          y: MOTION.distance.md,
          duration: MOTION.duration.medium,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        }, '-=0.2');
    });

    // Mobile (< 640px)
    mm.add('(max-width: 639px)', () => {
      const aboutTL = gsap.timeline({
        scrollTrigger: {
          trigger: '.avx-about',
          start: 'top 85%',
          toggleActions: 'play none none none'
        }
      });

      aboutTL
        .from(['.avx-about__meta', '.avx-about__title', '.avx-about__intro', '.avx-about__accent-rule'], {
          opacity: 0,
          y: 10,
          duration: MOTION.duration.fast + 0.15,
          stagger: 0.05,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        })
        .from('.avx-about__narrative > *', {
          opacity: 0,
          y: 10,
          duration: MOTION.duration.fast + 0.15,
          stagger: 0.05,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        }, '-=0.2')
        .from('.avx-about__media', {
          opacity: 0,
          y: 12,
          duration: MOTION.duration.medium,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        }, '-=0.2');
    });
  }

  /**
   * 4. PRODUCTS & SERVICES SECTION ANIMATIONS
   * Requirement:
   *  Section heading reveals first, then 9 cards stagger row-by-row via ScrollTrigger.batch().
   *  Do not animate all 9 simultaneously.
   */
  function initProductAnimations() {
    const productsSection = document.querySelector('.avx-products');
    if (!productsSection || typeof ScrollTrigger === 'undefined') return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    // 1. Header Reveal (Meta, Title, Intro, Accent Rule)
    const prodHeaderTL = gsap.timeline({
      scrollTrigger: {
        trigger: '.avx-products',
        start: 'top 78%',
        toggleActions: 'play none none none'
      }
    });

    prodHeaderTL
      .from('.avx-products__meta', {
        opacity: 0,
        y: MOTION.distance.sm,
        duration: MOTION.duration.medium,
        ease: MOTION.ease.editorial,
        clearProps: 'transform,opacity'
      })
      .from('.avx-products__title', {
        opacity: 0,
        y: MOTION.distance.md,
        duration: MOTION.duration.reveal,
        ease: MOTION.ease.editorial,
        clearProps: 'transform,opacity'
      }, '-=0.35')
      .from('.avx-products__intro', {
        opacity: 0,
        y: MOTION.distance.sm,
        duration: MOTION.duration.medium,
        ease: MOTION.ease.editorial,
        clearProps: 'transform,opacity'
      }, '-=0.4')
      .from('.avx-products__accent-rule', {
        scaleX: 0,
        duration: MOTION.duration.medium,
        ease: MOTION.ease.inOut,
        clearProps: 'transform'
      }, '-=0.3');

    // 2. Row-by-Row Card Entrance via ScrollTrigger.batch()
    // Staggers each visible row as it enters the viewport instead of animating all 9 simultaneously.
    ScrollTrigger.batch('.avx-product-card', {
      start: 'top 88%',
      once: true,
      onEnter: (batch) => {
        gsap.from(batch, {
          opacity: 0,
          y: MOTION.distance.lg,
          scale: 0.97,
          duration: MOTION.duration.medium,
          stagger: 0.08,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        });
      }
    });
  }

  /**
   * 5. WHAT WE STAND FOR SECTION (Editorial Architectural Presentation)
   * Progressive Spine, Sequential Reveal, Scroll-Tracked Active States,
   * Synchronized Hover & Keyboard Focus
   */
  function initValuesAnimations() {
    const valuesSection = document.querySelector('.avx-values');
    if (!valuesSection || typeof ScrollTrigger === 'undefined') return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const mm = gsap.matchMedia();
    const valueItems = gsap.utils.toArray('.avx-value');
    const manifestoDots = document.querySelectorAll('.avx-values__manifesto-dots span');

    // Central function to update active value across scroll, hover & keyboard focus
    function setActiveValue(index) {
      valueItems.forEach((item) => {
        const iIdx = parseInt(item.getAttribute('data-value-index'), 10);
        if (iIdx === index) {
          item.classList.add('is-active');
        } else {
          item.classList.remove('is-active');
        }
      });

      manifestoDots.forEach((dot) => {
        const dIdx = parseInt(dot.getAttribute('data-dot'), 10);
        if (dIdx === index) {
          dot.classList.add('is-active');
        } else {
          dot.classList.remove('is-active');
        }
      });
    }

    // Attach interactive hover & keyboard listeners
    valueItems.forEach((item) => {
      item.addEventListener('mouseenter', () => {
        const idx = parseInt(item.getAttribute('data-value-index'), 10);
        setActiveValue(idx);
      });
      item.addEventListener('focus', () => {
        const idx = parseInt(item.getAttribute('data-value-index'), 10);
        setActiveValue(idx);
      });
    });

    // Desktop Breakpoint (≥ 992px): Editorial Entrance + Continuous Spine Triggers
    mm.add('(min-width: 992px)', () => {
      // 1. Header & Manifesto entrance
      const headerTL = gsap.timeline({
        scrollTrigger: {
          trigger: '.avx-values',
          start: 'top 75%',
          toggleActions: 'play none none none'
        }
      });

      headerTL
        .from(['.avx-values__meta', '.avx-values__title', '.avx-values__intro', '.avx-values__accent-rule'], {
          opacity: 0,
          y: MOTION.distance.sm,
          duration: MOTION.duration.fast + 0.1,
          stagger: 0.06,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        })
        .from('.avx-values__manifesto', {
          opacity: 0,
          y: MOTION.distance.sm,
          duration: MOTION.duration.fast + 0.1,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        }, '-=0.2');

      // 2. Sequential Value Pillar Entrance & Active Triggers
      valueItems.forEach((item) => {
        const badge = item.querySelector('.avx-value__badge');
        const itemTL = gsap.timeline({
          scrollTrigger: {
            trigger: item,
            start: 'top 85%',
            toggleActions: 'play none none none'
          }
        });

        itemTL.from(item, {
          opacity: 0,
          y: 24,
          duration: MOTION.duration.medium,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        });

        if (badge) {
          itemTL.from(badge, {
            scale: 0.92,
            duration: MOTION.duration.fast + 0.1,
            ease: MOTION.ease.decel,
            clearProps: 'transform'
          }, '-=0.35');
        }

        // Active State ScrollTrigger
        const idx = parseInt(item.getAttribute('data-value-index'), 10);
        ScrollTrigger.create({
          trigger: item,
          start: 'top 52%',
          end: 'bottom 52%',
          onEnter: () => setActiveValue(idx),
          onEnterBack: () => setActiveValue(idx)
        });
      });
    });

    // Tablet Breakpoint (640px - 991px)
    mm.add('(min-width: 640px) and (max-width: 991px)', () => {
      const headerTL = gsap.timeline({
        scrollTrigger: {
          trigger: '.avx-values',
          start: 'top 80%',
          toggleActions: 'play none none none'
        }
      });

      headerTL
        .from(['.avx-values__meta', '.avx-values__title', '.avx-values__intro', '.avx-values__accent-rule'], {
          opacity: 0,
          y: MOTION.distance.sm,
          duration: MOTION.duration.medium,
          stagger: 0.06,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        })
        .from('.avx-values__manifesto', {
          opacity: 0,
          y: MOTION.distance.sm,
          duration: MOTION.duration.medium,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        }, '-=0.2');

      valueItems.forEach((item) => {
        gsap.from(item, {
          scrollTrigger: {
            trigger: item,
            start: 'top 88%',
            toggleActions: 'play none none none'
          },
          opacity: 0,
          y: MOTION.distance.md,
          duration: MOTION.duration.medium,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        });

        const idx = parseInt(item.getAttribute('data-value-index'), 10);
        ScrollTrigger.create({
          trigger: item,
          start: 'top 55%',
          end: 'bottom 55%',
          onEnter: () => setActiveValue(idx),
          onEnterBack: () => setActiveValue(idx)
        });
      });
    });

    // Mobile Breakpoint (< 640px)
    mm.add('(max-width: 639px)', () => {
      const headerTL = gsap.timeline({
        scrollTrigger: {
          trigger: '.avx-values',
          start: 'top 85%',
          toggleActions: 'play none none none'
        }
      });

      headerTL
        .from(['.avx-values__meta', '.avx-values__title', '.avx-values__intro', '.avx-values__accent-rule'], {
          opacity: 0,
          y: 10,
          duration: MOTION.duration.fast + 0.15,
          stagger: 0.05,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        });

      valueItems.forEach((item) => {
        gsap.from(item, {
          scrollTrigger: {
            trigger: item,
            start: 'top 90%',
            toggleActions: 'play none none none'
          },
          opacity: 0,
          y: 14,
          duration: MOTION.duration.medium,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        });

        const idx = parseInt(item.getAttribute('data-value-index'), 10);
        ScrollTrigger.create({
          trigger: item,
          start: 'top 60%',
          end: 'bottom 60%',
          onEnter: () => setActiveValue(idx),
          onEnterBack: () => setActiveValue(idx)
        });
      });
    });
  }

  /**
   * 6. CONTACT US & ENQUIRY FORM ANIMATIONS
   * Requirement:
   *  Lateral split convergence on desktop (Left x: -20px, Right x: 20px -> 0) with opacity and clearProps.
   *  Tablet & Mobile: Independent vertical reveals without lateral translation.
   */
  function initContactAnimations() {
    const contactSection = document.querySelector('.avx-contact');
    if (!contactSection || typeof ScrollTrigger === 'undefined') return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const mm = gsap.matchMedia();

    // Desktop (≥ 992px): Split-screen lateral convergence (Left x: -20, Right x: 20)
    mm.add('(min-width: 992px)', () => {
      const contactTL = gsap.timeline({
        scrollTrigger: {
          trigger: '.avx-contact',
          start: 'top 75%',
          toggleActions: 'play none none none'
        }
      });

      contactTL
        .from(['.avx-contact__meta', '.avx-contact__title', '.avx-contact__accent-rule'], {
          opacity: 0,
          y: MOTION.distance.sm,
          duration: MOTION.duration.medium,
          stagger: 0.05,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        }, 0)
        .from(['.avx-contact__lead', '.avx-contact__desc', '.avx-contact__caps'], {
          opacity: 0,
          y: MOTION.distance.sm,
          stagger: 0.05,
          duration: MOTION.duration.medium,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        }, 0.1)
        .from('.avx-contact__panel', {
          opacity: 0,
          y: MOTION.distance.md,
          duration: MOTION.duration.medium,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        }, 0.05)
        .from('.avx-contact__form-header, .avx-contact__row, .avx-contact__form > .avx-contact__field, .avx-contact__submit-wrap', {
          opacity: 0,
          y: 10,
          stagger: 0.03,
          duration: MOTION.duration.fast + 0.1,
          ease: MOTION.ease.decel,
          clearProps: 'transform,opacity'
        }, 0.15);
    });

    // Tablet (640px – 991px): Stacked layout with independent vertical reveals
    mm.add('(min-width: 640px) and (max-width: 991px)', () => {
      gsap.from('.avx-contact__aside-inner > *', {
        scrollTrigger: {
          trigger: '.avx-contact__aside',
          start: 'top 80%',
          toggleActions: 'play none none none'
        },
        opacity: 0,
        y: MOTION.distance.md,
        stagger: 0.08,
        duration: MOTION.duration.medium,
        ease: MOTION.ease.decel,
        clearProps: 'transform,opacity'
      });

      gsap.from('.avx-contact__panel-inner > *', {
        scrollTrigger: {
          trigger: '.avx-contact__panel',
          start: 'top 85%',
          toggleActions: 'play none none none'
        },
        opacity: 0,
        y: MOTION.distance.md,
        stagger: 0.08,
        duration: MOTION.duration.medium,
        ease: MOTION.ease.decel,
        clearProps: 'transform,opacity'
      });
    });

    // Mobile (< 640px): Subtle vertical entrance
    mm.add('(max-width: 639px)', () => {
      gsap.from('.avx-contact__aside-inner > *', {
        scrollTrigger: {
          trigger: '.avx-contact__aside',
          start: 'top 85%',
          toggleActions: 'play none none none'
        },
        opacity: 0,
        y: MOTION.distance.sm,
        stagger: 0.06,
        duration: MOTION.duration.medium,
        ease: MOTION.ease.decel,
        clearProps: 'transform,opacity'
      });

      gsap.from('.avx-contact__panel-inner > *', {
        scrollTrigger: {
          trigger: '.avx-contact__panel',
          start: 'top 88%',
          toggleActions: 'play none none none'
        },
        opacity: 0,
        y: MOTION.distance.sm,
        stagger: 0.06,
        duration: MOTION.duration.medium,
        ease: MOTION.ease.decel,
        clearProps: 'transform,opacity'
      });
    });
  }

  /**
   * 7. FOOTER UNDERSTATED SCROLL REVEAL & BACK TO TOP
   * Pre-banner call to action, staggered columns, bottom legal bar
   */
  function initFooterAnimations() {
    const footer = document.querySelector('.avx-footer');
    if (!footer || typeof ScrollTrigger === 'undefined') return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    // 1. Pre-Banner Reveal (if present)
    const preBanner = document.querySelector('.avx-footer__pre');
    if (preBanner) {
      gsap.from(['.avx-footer__pre-title', '.avx-footer__pre-desc', '.avx-footer__pre .avx-btn'], {
        scrollTrigger: {
          trigger: preBanner,
          start: 'top 88%',
          toggleActions: 'play none none none'
        },
        opacity: 0,
        y: MOTION.distance.sm,
        stagger: 0.08,
        duration: MOTION.duration.medium,
        ease: MOTION.ease.decel,
        clearProps: 'transform,opacity'
      });
    }

    // 2. Footer Columns Reveal
    gsap.from('.avx-footer__grid > div', {
      scrollTrigger: {
        trigger: '.avx-footer__main',
        start: 'top 88%',
        toggleActions: 'play none none none'
      },
      opacity: 0,
      y: MOTION.distance.md,
      stagger: 0.08,
      duration: MOTION.duration.medium,
      ease: MOTION.ease.decel,
      clearProps: 'transform,opacity'
    });

    // 3. Bottom Legal Bar Reveal
    gsap.from('.avx-footer__bottom', {
      scrollTrigger: {
        trigger: '.avx-footer__bottom',
        start: 'top 95%',
        toggleActions: 'play none none none'
      },
      opacity: 0,
      duration: MOTION.duration.medium,
      ease: MOTION.ease.decel,
      clearProps: 'opacity'
    });
  }

  /**
   * Resize, Orientation, & Font-Load Safety Listeners
   */
  function initSafetyHandlers() {
    if (typeof ScrollTrigger === 'undefined') return;

    // Debounce utility
    function debounce(func, wait) {
      let timeout;
      return function (...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
      };
    }

    // Debounced resize handler
    window.addEventListener('resize', debounce(() => {
      ScrollTrigger.refresh();
    }, 200), { passive: true });

    // Mobile orientation change handler
    window.addEventListener('orientationchange', () => {
      setTimeout(() => {
        ScrollTrigger.refresh();
      }, 300);
    }, { passive: true });

    // Font load handler: recalculates scroll triggers once custom web fonts are rendered
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(() => {
        ScrollTrigger.refresh();
      });
    }

    // Dynamic prefers-reduced-motion listener
    const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    if (motionQuery.addEventListener) {
      motionQuery.addEventListener('change', (e) => {
        if (e.matches) {
          applyReducedMotionState();
          ScrollTrigger.getAll().forEach(t => t.kill());
        } else {
          initAvenrixAnimations();
        }
      });
    }
  }

  // Expose modular controllers on window for accessibility and testability
  window.initAvenrixAnimations = initAvenrixAnimations;
  window.initHeaderAnimations = initHeaderAnimations;
  window.initHeroAnimations = initHeroAnimations;
  window.initAboutAnimations = initAboutAnimations;
  window.initProductAnimations = initProductAnimations;
  window.initValuesAnimations = initValuesAnimations;
  window.initContactAnimations = initContactAnimations;
  window.initFooterAnimations = initFooterAnimations;
})();
