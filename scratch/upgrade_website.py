# -*- coding: utf-8 -*-
"""
AVENRIX HEALTHCARE SOLUTIONS - WEBSITE UPGRADE SCRIPT
Upgrades index.html in place to 100% adhere to Avenrix_Antigravity_Website_Upgrade_Brief.docx
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# -----------------------------------------------------------------------------
# 1. Title & Meta Description (Section 8 of Brief)
# -----------------------------------------------------------------------------
html = re.sub(
    r'<title>.*?</title>',
    '<title>Avenrix Healthcare Solutions | Turnkey Healthcare Infrastructure</title>',
    html,
    count=1
)

html = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Avenrix Healthcare Solutions coordinates turnkey healthcare and pharmaceutical infrastructure solutions, including HVAC, modular OT, MGPS, cleanroom systems and medical equipment.">',
    html,
    count=1
)

# -----------------------------------------------------------------------------
# 2. Stylesheets in <head>
# -----------------------------------------------------------------------------
css_insert = """  <link rel="stylesheet" href="css/products.css">
  <link rel="stylesheet" href="css/industries.css">
  <link rel="stylesheet" href="css/approach.css">
  <link rel="stylesheet" href="css/quality.css">
  <link rel="stylesheet" href="css/values.css">
  <link rel="stylesheet" href="css/partnerships.css">
  <link rel="stylesheet" href="css/faqs.css">
  <link rel="stylesheet" href="css/contact.css">
  <link rel="stylesheet" href="css/footer.css">"""

html = re.sub(
    r'  <link rel="stylesheet" href="css/products\.css">.*?<link rel="stylesheet" href="css/footer\.css">',
    css_insert,
    html,
    flags=re.DOTALL
)

# -----------------------------------------------------------------------------
# 3. Desktop Header Navigation & Mobile Drawer (Section 3 of Brief)
# -----------------------------------------------------------------------------
desktop_nav = """      <!-- Desktop Navigation Menu -->
      <nav class="avx-header__nav" aria-label="Primary Navigation">
        <ul class="avx-header__nav-list">
          <li class="avx-header__nav-item"><a href="#about" class="avx-header__nav-link">About Us</a></li>
          <li class="avx-header__nav-item"><a href="#solutions" class="avx-header__nav-link">Solutions</a></li>
          <li class="avx-header__nav-item"><a href="#products" class="avx-header__nav-link">Products</a></li>
          <li class="avx-header__nav-item"><a href="#industries" class="avx-header__nav-link">Industries</a></li>
          <li class="avx-header__nav-item"><a href="#approach" class="avx-header__nav-link">Approach</a></li>
          <li class="avx-header__nav-item"><a href="#quality" class="avx-header__nav-link">Quality</a></li>
          <li class="avx-header__nav-item"><a href="#why-avenrix" class="avx-header__nav-link">Why Avenrix</a></li>
          <li class="avx-header__nav-item"><a href="#faqs" class="avx-header__nav-link">FAQs</a></li>
          <li class="avx-header__nav-item"><a href="#contact" class="avx-header__nav-link">Contact</a></li>
        </ul>
      </nav>"""

html = re.sub(
    r'      <!-- Desktop Navigation Menu.*?<\/nav>',
    desktop_nav,
    html,
    flags=re.DOTALL
)

drawer_nav = """      <ul class="avx-drawer__list">
        <li class="avx-drawer__item"><a href="#home" class="avx-drawer__link is-active">01. Home</a></li>
        <li class="avx-drawer__item"><a href="#about" class="avx-drawer__link">02. About Us</a></li>
        <li class="avx-drawer__item"><a href="#solutions" class="avx-drawer__link">03. Our Solutions</a></li>
        <li class="avx-drawer__item"><a href="#products" class="avx-drawer__link">04. Products</a></li>
        <li class="avx-drawer__item"><a href="#industries" class="avx-drawer__link">05. Industries We Serve</a></li>
        <li class="avx-drawer__item"><a href="#approach" class="avx-drawer__link">06. Our Approach</a></li>
        <li class="avx-drawer__item"><a href="#quality" class="avx-drawer__link">07. Quality Assurance</a></li>
        <li class="avx-drawer__item"><a href="#why-avenrix" class="avx-drawer__link">08. Why Avenrix</a></li>
        <li class="avx-drawer__item"><a href="#partnerships" class="avx-drawer__link">09. Partnerships</a></li>
        <li class="avx-drawer__item"><a href="#faqs" class="avx-drawer__link">10. FAQs</a></li>
        <li class="avx-drawer__item"><a href="#contact" class="avx-drawer__link">11. Contact Us</a></li>
      </ul>"""

html = re.sub(
    r'      <ul class="avx-drawer__list">.*?<\/ul>',
    drawer_nav,
    html,
    flags=re.DOTALL
)

print("Nav & Head updated.")

# -----------------------------------------------------------------------------
# 4. Section 01: Home (#home) - Section 4.1 of Brief
# -----------------------------------------------------------------------------
home_section = """    <!-- ======================================================================
         SECTION 01: HOME
         ====================================================================== -->
    <section class="avx-hero" id="home" aria-label="Hero Introduction">
      <!-- Architectural Grid Decorative Background -->
      <div class="avx-hero__grid-bg" aria-hidden="true"></div>

      <div class="avx-container avx-hero__container">
        <div class="avx-hero__layout">
          <!-- Left Column: Editorial Headline & Copy -->
          <div class="avx-hero__content">
            <div class="avx-hero__eyebrow avx-eyebrow">
              <span>Healthcare Infrastructure Solutions</span>
            </div>
            
            <h1 class="avx-hero__title">
              Engineering Healthcare. <span class="avx-hero__title-accent">Building Trust.</span>
            </h1>

            <p style="font-family: var(--avx-font-sans); font-size: clamp(1rem, 1.2vw + 0.5rem, 1.25rem); font-weight: 600; color: var(--avx-corp-navy); margin-bottom: var(--avx-space-3); line-height: 1.35;">
              Complete Turnkey Healthcare &amp; Pharmaceutical Infrastructure Solutions
            </p>

            <p class="avx-hero__desc">
              At Avenrix Healthcare Solutions, we bring together specialized products, technical expertise and reliable manufacturing partnerships to deliver comprehensive infrastructure solutions for healthcare and pharmaceutical environments. From HVAC and modular operation theatres to medical gas pipeline systems, cleanroom infrastructure and specialized medical equipment, we help transform complex infrastructure requirements into coordinated, dependable solutions.
            </p>

            <div class="avx-hero__ctas">
              <a href="#solutions" class="avx-btn avx-btn--primary avx-hero__btn-primary">
                <span>Explore Our Solutions</span>
                <svg class="avx-icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
                  <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </a>
              <a href="#contact" class="avx-btn avx-btn--secondary avx-hero__btn-secondary">
                <span>Request a Consultation</span>
              </a>
              <a href="Avenrix-Healthcare-Solutions-Brochure.pdf" download class="avx-hero__btn-brochure" aria-label="Download Avenrix Company Brochure PDF">
                <svg width="16" height="16" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                  <path d="M4 17h12M10 3v10m0 0l-3.5-3.5M10 13l3.5-3.5"/>
                </svg>
                <span>Download Brochure</span>
              </a>
            </div>
          </div>

          <!-- Right Column: Precision Technical Visual Frame -->
          <div class="avx-hero__visual-wrapper">
            <div class="avx-hero__visual" id="heroVisual">
              <!-- Card Header Bar -->
              <div class="avx-hero__visual-meta">
                <span class="avx-hero__visual-id">SYS-REF // CRITICAL INFRASTRUCTURE</span>
                <span class="avx-hero__visual-status">
                  <span class="avx-hero__status-pulse" aria-hidden="true"></span>
                  <span>PROJECT COORDINATION</span>
                </span>
              </div>

              <!-- Schematic Graphic Container -->
              <div class="avx-hero__schematic">
                <img 
                  src="images/hero.jpg" 
                  alt="Avenrix Healthcare Infrastructure Solutions Overview" 
                  class="avx-hero__schematic-img" 
                  width="800" 
                  height="600"
                  decoding="async"
                >
              </div>

              <!-- Technical Specification Footer -->
              <div class="avx-hero__visual-spec">
                <div class="avx-hero__spec-item">
                  <span class="avx-hero__spec-label">DOMAIN</span>
                  <span class="avx-hero__spec-val">TURNKEY INFRASTRUCTURE</span>
                </div>
                <div class="avx-hero__spec-item">
                  <span class="avx-hero__spec-label">SOURCING</span>
                  <span class="avx-hero__spec-val">VETTED PARTNERS</span>
                </div>
                <div class="avx-hero__spec-item">
                  <span class="avx-hero__spec-label">EXECUTION</span>
                  <span class="avx-hero__spec-val">COORDINATED SUPPORT</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Homepage Introduction & Highlight Cards (Section 4.1) -->
        <div class="avx-hero-intro">
          <div class="avx-hero-intro__header">
            <h2 class="avx-hero-intro__title">Building the Infrastructure Behind Better Healthcare</h2>
            <p class="avx-hero-intro__lead">
              Healthcare infrastructure requires precision, reliability and uncompromising attention to quality. At Avenrix, we understand that every healthcare environment has unique technical and operational requirements. Our approach focuses on understanding project needs, identifying suitable manufacturing partners, coordinating product supply and supporting installation and commissioning activities. We aim to make healthcare infrastructure projects simpler, more coordinated and more dependable.
            </p>
          </div>

          <div class="avx-hero-intro__grid" role="list">
            <a href="#solutions" class="avx-intro-card" role="listitem">
              <div class="avx-intro-card__media">
                <img src="images/products/02 AHU - Air Handling Unit.jpg" alt="HVAC & AHU Solutions" class="avx-intro-card__img" loading="lazy" decoding="async">
              </div>
              <div class="avx-intro-card__body">
                <h3 class="avx-intro-card__title">HVAC &amp; AHU Solutions</h3>
                <p class="avx-intro-card__desc">Controlled ventilation and air management systems.</p>
                <span class="avx-intro-card__link">
                  <span>Explore Solutions</span>
                  <svg viewBox="0 0 16 16" fill="none"><path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </span>
              </div>
            </a>

            <a href="#solutions" class="avx-intro-card" role="listitem">
              <div class="avx-intro-card__media">
                <img src="images/products/04 Modulalr Operation Theater.jpg" alt="Modular Operation Theatres" class="avx-intro-card__img" loading="lazy" decoding="async">
              </div>
              <div class="avx-intro-card__body">
                <h3 class="avx-intro-card__title">Modular Operation Theatres</h3>
                <p class="avx-intro-card__desc">Integrated OT infrastructure and equipment.</p>
                <span class="avx-intro-card__link">
                  <span>Explore Solutions</span>
                  <svg viewBox="0 0 16 16" fill="none"><path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </span>
              </div>
            </a>

            <a href="#solutions" class="avx-intro-card" role="listitem">
              <div class="avx-intro-card__media">
                <img src="images/products/08 Wall &amp; Ceiling Panels.jpg" alt="Modular Infrastructure" class="avx-intro-card__img" loading="lazy" decoding="async">
              </div>
              <div class="avx-intro-card__body">
                <h3 class="avx-intro-card__title">Modular Infrastructure</h3>
                <p class="avx-intro-card__desc">Wall panels, ceilings, flooring and doors.</p>
                <span class="avx-intro-card__link">
                  <span>Explore Solutions</span>
                  <svg viewBox="0 0 16 16" fill="none"><path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </span>
              </div>
            </a>

            <a href="#solutions" class="avx-intro-card" role="listitem">
              <div class="avx-intro-card__media">
                <img src="images/products/07 Medical Gas Pipeline System.jpg" alt="Medical Gas Pipeline Systems" class="avx-intro-card__img" loading="lazy" decoding="async">
              </div>
              <div class="avx-intro-card__body">
                <h3 class="avx-intro-card__title">Medical Gas Pipeline Systems</h3>
                <p class="avx-intro-card__desc">Medical gas distribution infrastructure.</p>
                <span class="avx-intro-card__link">
                  <span>Explore Solutions</span>
                  <svg viewBox="0 0 16 16" fill="none"><path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </span>
              </div>
            </a>
          </div>
        </div>
      </div>
    </section>"""

html = re.sub(
    r'<section class="avx-hero" id="home".*?<\/section>',
    home_section,
    html,
    flags=re.DOTALL
)

print("Section 01 (Home) updated.")

# -----------------------------------------------------------------------------
# 5. Section 02: About Avenrix (#about) - Section 4.2 of Brief
# -----------------------------------------------------------------------------
about_section = """    <!-- ======================================================================
         SECTION 02: ABOUT AVENRIX
         ====================================================================== -->
    <section class="avx-about" id="about" aria-label="About Avenrix Healthcare Solutions">
      <!-- Subtle Architectural Watermark Grid -->
      <div class="avx-about__bg-grid" aria-hidden="true"></div>

      <div class="avx-container avx-about__container">
        <!-- Top Editorial Block -->
        <div class="avx-about__header">
          <div class="avx-about__meta">
            <div class="avx-eyebrow avx-about__eyebrow">
              <span>About Avenrix</span>
            </div>
          </div>

          <h2 class="avx-about__title">
            Your Trusted Healthcare &amp; Pharmaceutical <span class="avx-about__title-accent">Infrastructure Solutions Provider</span>
          </h2>

          <div class="avx-about__accent-rule" aria-hidden="true"></div>
        </div>

        <!-- Asymmetric Editorial Body Layout (Who We Are per 4.2) -->
        <div class="avx-about__layout">
          <!-- Left Column: Who We Are Structured Narrative -->
          <div class="avx-about__narrative">
            <div class="avx-about__lead-card">
              <p class="avx-about__lead-text" style="font-weight: 500; font-size: 1.05rem; color: var(--avx-navy); margin-bottom: var(--avx-space-4);">
                Avenrix Healthcare Solutions is a healthcare infrastructure solutions company focused on delivering integrated products and turnkey solutions for hospitals, pharmaceutical facilities and specialized healthcare environments.
              </p>
              <p class="avx-about__lead-text" style="color: var(--avx-slate-700); margin-bottom: var(--avx-space-4);">
                We bring together specialized manufacturers, technical resources and project coordination to address diverse infrastructure requirements under one platform.
              </p>
              <p class="avx-about__lead-text" style="color: var(--avx-slate-700); margin-bottom: var(--avx-space-4);">
                Our approach is built around understanding client requirements, sourcing suitable products, coordinating with manufacturing partners and supporting project execution.
              </p>
              <p class="avx-about__lead-text" style="color: var(--avx-slate-700); margin: 0;">
                We believe that dependable healthcare infrastructure begins with the right products, the right technical approach and the right partnerships.
              </p>
            </div>

            <!-- Single-Point Project Accountability -->
            <div class="avx-about__execution" style="margin-top: var(--avx-space-6);">
              <div class="avx-about__execution-header">
                <svg class="avx-icon" width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                  <path d="M10 2V6M10 14V18M2 10H6M14 10H18M4.93 4.93L7.76 7.76M12.24 12.24L15.07 15.07M4.93 15.07L7.76 12.24M12.24 7.76L15.07 4.93" stroke="var(--avx-blue)" stroke-width="1.8" stroke-linecap="round"/>
                </svg>
                <h3 class="avx-about__execution-title" style="margin: 0;">Turnkey Coordination &amp; Execution</h3>
              </div>
              <p class="avx-about__execution-text">
                From initial project scope review and specification alignment to product sourcing, delivery coordination and commissioning support, we provide coordinated infrastructure execution tailored to project requirements.
              </p>
            </div>
          </div>

          <!-- Right Column: Architectural Visual Frame -->
          <div class="avx-about__visual-col">
            <div class="avx-about__media">
              <div class="avx-about__media-meta">
                <span>ARCH-REF // INFRASTRUCTURE MODEL</span>
                <span class="avx-about__media-status">
                  <span class="avx-about__media-dot" aria-hidden="true"></span>
                  <span>SYSTEM CROSS-SECTION</span>
                </span>
              </div>

              <div class="avx-about__image-frame">
                <img 
                  src="images/aboutus.jpg" 
                  alt="Avenrix Critical Healthcare Infrastructure and Modular Cleanroom Installation" 
                  class="avx-about__image" 
                  width="800" 
                  height="600"
                  loading="lazy"
                  decoding="async"
                >
              </div>

              <div class="avx-about__media-specs">
                <div class="avx-about__spec-col">
                  <span class="avx-about__spec-label">MODEL</span>
                  <span class="avx-about__spec-val">Sourcing &amp; Coordination</span>
                </div>
                <div class="avx-about__spec-col">
                  <span class="avx-about__spec-label">ENVIRONMENTS</span>
                  <span class="avx-about__spec-val">Hospitals &amp; Pharma</span>
                </div>
                <div class="avx-about__spec-col">
                  <span class="avx-about__spec-label">STANDARDS</span>
                  <span class="avx-about__spec-val">Project-Specific Alignment</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Vision, Mission & Philosophy (Section 4.2 Approved Copy) -->
        <div class="avx-about__extensions">
          <!-- Left Column: Vision & Mission (All 5 Statements) -->
          <div class="avx-about__vision-mission">
            <!-- Our Vision -->
            <div class="avx-about__vision-card">
              <h3 class="avx-about__block-title">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>
                <span>Our Vision</span>
              </h3>
              <p class="avx-about__vision-text">
                To become a trusted name in healthcare and pharmaceutical infrastructure by delivering reliable, innovative and quality-focused solutions.
              </p>
            </div>

            <!-- Our Mission (All 5 Approved Statements) -->
            <div class="avx-about__mission-card">
              <h3 class="avx-about__block-title">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
                <span>Our Mission</span>
              </h3>
              <ul class="avx-about__mission-list" role="list">
                <li class="avx-about__mission-item">
                  <span class="avx-about__mission-item-dot" aria-hidden="true"></span>
                  <span>To provide comprehensive healthcare infrastructure solutions under one platform.</span>
                </li>
                <li class="avx-about__mission-item">
                  <span class="avx-about__mission-item-dot" aria-hidden="true"></span>
                  <span>To connect clients with specialized and dependable manufacturing partners.</span>
                </li>
                <li class="avx-about__mission-item">
                  <span class="avx-about__mission-item-dot" aria-hidden="true"></span>
                  <span>To promote quality, technical suitability and transparency.</span>
                </li>
                <li class="avx-about__mission-item">
                  <span class="avx-about__mission-item-dot" aria-hidden="true"></span>
                  <span>To simplify infrastructure procurement and project coordination.</span>
                </li>
                <li class="avx-about__mission-item">
                  <span class="avx-about__mission-item-dot" aria-hidden="true"></span>
                  <span>To build long-term relationships through reliability and professional service.</span>
                </li>
              </ul>
            </div>
          </div>

          <!-- Right Column: Our Philosophy Callout Box (Exact Approved Quote) -->
          <div class="avx-about__philosophy-card">
            <span class="avx-about__philosophy-label">Our Philosophy</span>
            <div class="avx-about__philosophy-headline">
              ENGINEERING HEALTHCARE. BUILDING TRUST.
            </div>
            <p class="avx-about__philosophy-body">
              For us, this is more than a tagline. It represents our commitment to building dependable relationships and supporting the infrastructure that healthcare facilities rely on every day.
            </p>
          </div>
        </div>
      </div>
    </section>"""

html = re.sub(
    r'<section class="avx-about" id="about".*?<\/section>',
    about_section,
    html,
    flags=re.DOTALL
)

print("Section 02 (About) updated.")

# -----------------------------------------------------------------------------
# 6. Section 03: Our Solutions (#solutions) - Section 4.3 of Brief
# -----------------------------------------------------------------------------
solutions_section = """    <!-- ======================================================================
         SECTION 03: OUR SOLUTIONS
         ====================================================================== -->
    <section class="avx-solutions" id="solutions" aria-label="Our Healthcare Infrastructure Solutions">
      <!-- Subtle Architectural Watermark Grid -->
      <div class="avx-solutions__bg-grid" aria-hidden="true"></div>

      <div class="avx-container avx-solutions__container">
        <!-- Section Header Block -->
        <div class="avx-solutions__header">
          <div class="avx-solutions__eyebrow avx-eyebrow">
            <span>Our Solutions</span>
          </div>

          <h2 class="avx-solutions__title">
            Integrated Solutions for <span class="avx-solutions__title-accent">Every Healthcare Environment</span>
          </h2>

          <p class="avx-solutions__intro">
            Avenrix offers coordinated infrastructure solutions designed to address the diverse requirements of modern healthcare and pharmaceutical facilities.
          </p>

          <div class="avx-solutions__accent-rule" aria-hidden="true"></div>
        </div>

        <!-- 6-Card Solutions Grid -->
        <div class="avx-solutions__grid" role="list">
          
          <!-- Solution 01: HVAC & AHU Solutions -->
          <article class="avx-solution-card" role="listitem">
            <div>
              <div class="avx-solution-card__sys-bar">
                <span class="avx-solution-card__code">SYS-01 // AIR-HVAC</span>
                <span class="avx-solution-card__badge-status">
                  <span class="avx-solution-card__dot" aria-hidden="true"></span>
                  AIR MANAGEMENT
                </span>
              </div>

              <div class="avx-solution-card__header">
                <div class="avx-solution-card__icon-wrap" aria-hidden="true">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"/>
                  </svg>
                </div>
                <span class="avx-solution-card__num" aria-hidden="true">01</span>
              </div>

              <h3 class="avx-solution-card__title">HVAC &amp; AHU Solutions</h3>
              <p class="avx-solution-card__desc">
                We provide HVAC and air handling solutions for specialized healthcare environments where ventilation, filtration, temperature and humidity management are important.
              </p>

              <div class="avx-solution-card__specs" aria-label="Target Environments">
                <div class="avx-solution-card__spec-item">
                  <span class="avx-solution-card__spec-label">Target Scopes</span>
                  <span class="avx-solution-card__spec-val">OTs, ICUs, NICU, SICU</span>
                </div>
                <div class="avx-solution-card__spec-item">
                  <span class="avx-solution-card__spec-label">Specialized Scopes</span>
                  <span class="avx-solution-card__spec-val">IVF Labs &amp; Pharma Facilities</span>
                </div>
              </div>
            </div>

            <div>
              <div class="avx-solution-card__features" aria-label="Key features">
                <span class="avx-solution-card__tag">Operation Theatres</span>
                <span class="avx-solution-card__tag">Critical ICUs</span>
                <span class="avx-solution-card__tag">IVF Laboratories</span>
                <span class="avx-solution-card__tag">Pharma Cleanrooms</span>
              </div>
              <div class="avx-solution-card__footer">
                <a href="#products" class="avx-solution-card__link" aria-label="View HVAC and AHU products and technical specs">
                  <span>View Products &amp; Specs</span>
                  <svg viewBox="0 0 16 16" fill="none" aria-hidden="true">
                    <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </a>
              </div>
            </div>
          </article>

          <!-- Solution 02: Modular Operation Theatres (OT) -->
          <article class="avx-solution-card" role="listitem">
            <div>
              <div class="avx-solution-card__sys-bar">
                <span class="avx-solution-card__code">SYS-02 // SURG-OT</span>
                <span class="avx-solution-card__badge-status">
                  <span class="avx-solution-card__dot" aria-hidden="true"></span>
                  SURGICAL SUITE
                </span>
              </div>

              <div class="avx-solution-card__header">
                <div class="avx-solution-card__icon-wrap" aria-hidden="true">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 3h18v18H3zM9 9h6v6H9z"/>
                    <path d="M12 9v6M9 12h6"/>
                  </svg>
                </div>
                <span class="avx-solution-card__num" aria-hidden="true">02</span>
              </div>

              <h3 class="avx-solution-card__title">Modular Operation Theatres (OT)</h3>
              <p class="avx-solution-card__desc">
                We coordinate complete modular operation theatre solutions designed to support infection-controlled, operationally efficient surgical environments.
              </p>

              <div class="avx-solution-card__specs" aria-label="Scope Components">
                <div class="avx-solution-card__spec-item">
                  <span class="avx-solution-card__spec-label">Enclosure Systems</span>
                  <span class="avx-solution-card__spec-val">Wall &amp; Ceiling Panels, Flooring</span>
                </div>
                <div class="avx-solution-card__spec-item">
                  <span class="avx-solution-card__spec-label">Surgical Integration</span>
                  <span class="avx-solution-card__spec-val">Laminar Airflow &amp; Control Panels</span>
                </div>
              </div>
            </div>

            <div>
              <div class="avx-solution-card__features" aria-label="Key features">
                <span class="avx-solution-card__tag">Modular OT Setup</span>
                <span class="avx-solution-card__tag">Laminar Airflow</span>
                <span class="avx-solution-card__tag">Hermetic Doors</span>
                <span class="avx-solution-card__tag">Control Panels</span>
              </div>
              <div class="avx-solution-card__footer">
                <a href="#products" class="avx-solution-card__link" aria-label="View Modular OT products and technical specs">
                  <span>View Products &amp; Specs</span>
                  <svg viewBox="0 0 16 16" fill="none" aria-hidden="true">
                    <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </a>
              </div>
            </div>
          </article>

          <!-- Solution 03: Modular Wall, Ceiling & Flooring Systems -->
          <article class="avx-solution-card" role="listitem">
            <div>
              <div class="avx-solution-card__sys-bar">
                <span class="avx-solution-card__code">SYS-03 // ARCH-MOD</span>
                <span class="avx-solution-card__badge-status">
                  <span class="avx-solution-card__dot" aria-hidden="true"></span>
                  ARCHITECTURAL
                </span>
              </div>

              <div class="avx-solution-card__header">
                <div class="avx-solution-card__icon-wrap" aria-hidden="true">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="2" y="3" width="20" height="18" rx="2"/>
                    <line x1="12" y1="3" x2="12" y2="21"/>
                  </svg>
                </div>
                <span class="avx-solution-card__num" aria-hidden="true">03</span>
              </div>

              <h3 class="avx-solution-card__title">Modular Wall, Ceiling &amp; Flooring</h3>
              <p class="avx-solution-card__desc">
                We supply and coordinate specialized architectural infrastructure for healthcare facilities, laboratories and cleanrooms.
              </p>

              <div class="avx-solution-card__specs" aria-label="Infrastructure Scope">
                <div class="avx-solution-card__spec-item">
                  <span class="avx-solution-card__spec-label">Panel Systems</span>
                  <span class="avx-solution-card__spec-val">HPL, Pre-Painted GI, SS</span>
                </div>
                <div class="avx-solution-card__spec-item">
                  <span class="avx-solution-card__spec-label">Joinery &amp; Seals</span>
                  <span class="avx-solution-card__spec-val">Hermetic Doors &amp; Covings</span>
                </div>
              </div>
            </div>

            <div>
              <div class="avx-solution-card__features" aria-label="Key features">
                <span class="avx-solution-card__tag">Modular Wall Panels</span>
                <span class="avx-solution-card__tag">Ceiling Systems</span>
                <span class="avx-solution-card__tag">Healthcare Flooring</span>
                <span class="avx-solution-card__tag">Hermetic Doors</span>
              </div>
              <div class="avx-solution-card__footer">
                <a href="#products" class="avx-solution-card__link" aria-label="View Modular Wall and Ceiling products and specs">
                  <span>View Products &amp; Specs</span>
                  <svg viewBox="0 0 16 16" fill="none" aria-hidden="true">
                    <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </a>
              </div>
            </div>
          </article>

          <!-- Solution 04: Medical Gas Pipeline Systems (MGPS) -->
          <article class="avx-solution-card" role="listitem">
            <div>
              <div class="avx-solution-card__sys-bar">
                <span class="avx-solution-card__code">SYS-04 // GAS-MGPS</span>
                <span class="avx-solution-card__badge-status">
                  <span class="avx-solution-card__dot" aria-hidden="true"></span>
                  MEDICAL GAS
                </span>
              </div>

              <div class="avx-solution-card__header">
                <div class="avx-solution-card__icon-wrap" aria-hidden="true">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
                  </svg>
                </div>
                <span class="avx-solution-card__num" aria-hidden="true">04</span>
              </div>

              <h3 class="avx-solution-card__title">Medical Gas Pipeline Systems</h3>
              <p class="avx-solution-card__desc">
                We offer medical gas pipeline infrastructure solutions for hospitals and healthcare facilities, subject to project specifications and applicable technical requirements.
              </p>

              <div class="avx-solution-card__specs" aria-label="MGPS Scope">
                <div class="avx-solution-card__spec-item">
                  <span class="avx-solution-card__spec-label">Distribution Units</span>
                  <span class="avx-solution-card__spec-val">Gas Manifolds &amp; Terminal Outlets</span>
                </div>
                <div class="avx-solution-card__spec-item">
                  <span class="avx-solution-card__spec-label">Safety &amp; Alarms</span>
                  <span class="avx-solution-card__spec-val">Area Valve Units &amp; Gas Alarms</span>
                </div>
              </div>
            </div>

            <div>
              <div class="avx-solution-card__features" aria-label="Key features">
                <span class="avx-solution-card__tag">Pipeline Network</span>
                <span class="avx-solution-card__tag">Gas Manifolds</span>
                <span class="avx-solution-card__tag">Medical Outlets</span>
                <span class="avx-solution-card__tag">Alarm Systems</span>
              </div>
              <div class="avx-solution-card__footer">
                <a href="#products" class="avx-solution-card__link" aria-label="View Medical Gas Pipeline products and specs">
                  <span>View Products &amp; Specs</span>
                  <svg viewBox="0 0 16 16" fill="none" aria-hidden="true">
                    <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </a>
              </div>
            </div>
          </article>

          <!-- Solution 05: Cleanroom & Pharmaceutical Infrastructure -->
          <article class="avx-solution-card" role="listitem">
            <div>
              <div class="avx-solution-card__sys-bar">
                <span class="avx-solution-card__code">SYS-05 // PHARMA-CR</span>
                <span class="avx-solution-card__badge-status">
                  <span class="avx-solution-card__dot" aria-hidden="true"></span>
                  CLEANROOM
                </span>
              </div>

              <div class="avx-solution-card__header">
                <div class="avx-solution-card__icon-wrap" aria-hidden="true">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
                  </svg>
                </div>
                <span class="avx-solution-card__num" aria-hidden="true">05</span>
              </div>

              <h3 class="avx-solution-card__title">Cleanroom &amp; Pharmaceutical</h3>
              <p class="avx-solution-card__desc">
                We support infrastructure requirements for pharmaceutical, laboratory and controlled-environment facilities.
              </p>

              <div class="avx-solution-card__specs" aria-label="Cleanroom Scope">
                <div class="avx-solution-card__spec-item">
                  <span class="avx-solution-card__spec-label">Air &amp; Envelope</span>
                  <span class="avx-solution-card__spec-val">Cleanroom HVAC &amp; HEPA Filtration</span>
                </div>
                <div class="avx-solution-card__spec-item">
                  <span class="avx-solution-card__spec-label">Utility &amp; Access</span>
                  <span class="avx-solution-card__spec-val">Pass Boxes, Doors, SS Storage</span>
                </div>
              </div>
            </div>

            <div>
              <div class="avx-solution-card__features" aria-label="Key features">
                <span class="avx-solution-card__tag">Cleanroom HVAC</span>
                <span class="avx-solution-card__tag">HEPA Filtration</span>
                <span class="avx-solution-card__tag">Pass Boxes</span>
                <span class="avx-solution-card__tag">SS Storage</span>
              </div>
              <div class="avx-solution-card__footer">
                <a href="#products" class="avx-solution-card__link" aria-label="View Cleanroom infrastructure products and specs">
                  <span>View Products &amp; Specs</span>
                  <svg viewBox="0 0 16 16" fill="none" aria-hidden="true">
                    <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </a>
              </div>
            </div>
          </article>

          <!-- Solution 06: Medical Equipment & Accessories -->
          <article class="avx-solution-card" role="listitem">
            <div>
              <div class="avx-solution-card__sys-bar">
                <span class="avx-solution-card__code">SYS-06 // MED-EQUIP</span>
                <span class="avx-solution-card__badge-status">
                  <span class="avx-solution-card__dot" aria-hidden="true"></span>
                  EQUIPMENT
                </span>
              </div>

              <div class="avx-solution-card__header">
                <div class="avx-solution-card__icon-wrap" aria-hidden="true">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="3"/>
                    <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/>
                  </svg>
                </div>
                <span class="avx-solution-card__num" aria-hidden="true">06</span>
              </div>

              <h3 class="avx-solution-card__title">Medical Equipment &amp; Accessories</h3>
              <p class="avx-solution-card__desc">
                We coordinate the supply of specialized medical equipment and accessories for modern healthcare facilities.
              </p>

              <div class="avx-solution-card__specs" aria-label="Equipment Scope">
                <div class="avx-solution-card__spec-item">
                  <span class="avx-solution-card__spec-label">Surgical &amp; Lighting</span>
                  <span class="avx-solution-card__spec-val">OT Lights, LED Lights, Pendants</span>
                </div>
                <div class="avx-solution-card__spec-item">
                  <span class="avx-solution-card__spec-label">Clinical Stations</span>
                  <span class="avx-solution-card__spec-val">Scrub Stations, X-ray View Boxes</span>
                </div>
              </div>
            </div>

            <div>
              <div class="avx-solution-card__features" aria-label="Key features">
                <span class="avx-solution-card__tag">OT Lights &amp; LED</span>
                <span class="avx-solution-card__tag">Surgeon Pendants</span>
                <span class="avx-solution-card__tag">Scrub Stations</span>
                <span class="avx-solution-card__tag">X-Ray View Boxes</span>
              </div>
              <div class="avx-solution-card__footer">
                <a href="#products" class="avx-solution-card__link" aria-label="View Medical Equipment and accessories catalogue">
                  <span>View Products &amp; Specs</span>
                  <svg viewBox="0 0 16 16" fill="none" aria-hidden="true">
                    <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </a>
              </div>
            </div>
          </article>

        </div>

        <!-- Compliance & Scope Control Footnote (Section 9 Guardrails) -->
        <div style="margin-top: var(--avx-space-8); padding: var(--avx-space-4) var(--avx-space-6); background: var(--avx-blue-tint); border-left: 3px solid var(--avx-blue); border-radius: var(--avx-radius-sm); font-size: var(--avx-text-xs); color: var(--avx-slate-600); line-height: 1.5;">
          * Solutions are planned, supplied and coordinated to align with verified project specifications, facility clinical needs and applicable healthcare standards (supporting NABH / cGMP compliance requirements).
        </div>
      </div>
    </section>"""

html = re.sub(
    r'<section class="avx-solutions" id="solutions".*?<\/section>',
    solutions_section,
    html,
    flags=re.DOTALL
)

print("Section 03 (Solutions) updated.")

# -----------------------------------------------------------------------------
# 7. Section 04: Products & Equipment (#products) - Section 4.4 of Brief
# Update Header + Add Bottom Product CTA Banner (Preserve Dual-Slider on Card 01)
# -----------------------------------------------------------------------------
products_header_old = """          <h2 class="avx-products__title">
            Specialized Products for <span class="avx-products__title-accent">Critical Healthcare Environments</span>
          </h2>

          <p class="avx-products__intro">
            Clean image-led portfolio of equipment and components sourced through verified manufacturing partners for turnkey healthcare and pharmaceutical installations.
          </p>"""

products_header_new = """          <h2 class="avx-products__title">
            Specialized Products. Integrated Infrastructure. <span class="avx-products__title-accent">One Reliable Partner.</span>
          </h2>

          <p class="avx-products__intro">
            Avenrix brings together a wide range of healthcare infrastructure products through specialized manufacturing and supply partnerships.
          </p>"""

if products_header_old in html:
    html = html.replace(products_header_old, products_header_new)

# Add Product Bottom CTA Banner before </section> of #products
product_cta_banner = """        <!-- Product CTA Banner (Section 4.4) -->
        <div class="avx-products__cta-banner">
          <div class="avx-products__cta-content">
            <h3 class="avx-products__cta-heading">Need technical specifications, product details or pricing?</h3>
            <p class="avx-products__cta-sub">Our technical specialists will provide tailored data sheets, equipment dimensions, and coordination proposals.</p>
          </div>
          <div class="avx-products__cta-action">
            <a href="#contact" class="avx-btn avx-btn--primary avx-products__cta-btn">
              <span>Request Product Information</span>
              <svg class="avx-icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
                <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </section>"""

html = re.sub(
    r'(\s*<\/div>\s*<\/section>\s*<!-- =+\s*SECTION 04: INDUSTRIES)',
    f'\n{product_cta_banner}\n\n    <!-- ======================================================================\n         SECTION 05: INDUSTRIES',
    html
)

print("Section 04 (Products) updated with 4.4 CTA banner.")

# -----------------------------------------------------------------------------
# 8. Section 05: Industries We Serve (#industries) - Section 4.5 of Brief
# Update Header + Update 7 Approved Industry Targets
# -----------------------------------------------------------------------------
industries_header_old = """          <h2 class="avx-industries__title">
            Tailored Solutions for Every <span class="avx-industries__title-accent">Healthcare &amp; Cleanroom Facility</span>
          </h2>

          <p class="avx-industries__intro">
            Our infrastructure solutions are engineered to meet the stringent regulatory and operational demands of specialized sectors:
          </p>"""

industries_header_new = """          <h2 class="avx-industries__title">
            Tailored Solutions for Every <span class="avx-industries__title-accent">Specialized Healthcare Environment</span>
          </h2>

          <p class="avx-industries__intro">
            Coordinated infrastructure solutions tailored to the operational demands and regulatory environments of specialized healthcare and pharmaceutical sectors.
          </p>"""

if industries_header_old in html:
    html = html.replace(industries_header_old, industries_header_new)

# -----------------------------------------------------------------------------
# 9. Inject Section 06: Our Approach & Execution Process (#approach)
# AND Section 07: Quality Assurance (#quality)
# (Injected immediately after #industries and before #why-avenrix)
# -----------------------------------------------------------------------------
approach_and_quality = """    <!-- ======================================================================
         SECTION 06: OUR APPROACH & EXECUTION PROCESS (Section 4.6)
         ====================================================================== -->
    <section class="avx-approach" id="approach" aria-label="Our Approach & Execution Process">
      <div class="avx-approach__bg-grid" aria-hidden="true"></div>

      <div class="avx-container avx-approach__container">
        <div class="avx-approach__header">
          <div class="avx-approach__eyebrow avx-eyebrow">
            <span>Execution Process</span>
          </div>

          <h2 class="avx-approach__title">
            From Concept to Completion: <span class="avx-approach__title-accent">Our Structured Approach</span>
          </h2>

          <p class="avx-approach__intro">
            We follow a structured approach to understand requirements and coordinate the right solutions for every project.
          </p>

          <div class="avx-approach__accent-rule" aria-hidden="true"></div>
        </div>

        <div class="avx-approach__grid" role="list">
          <!-- Step 01 -->
          <article class="avx-step-card" role="listitem">
            <div>
              <div class="avx-step-card__top">
                <span class="avx-step-card__num-badge">01</span>
                <span class="avx-step-card__stage">Phase 01 // Discovery</span>
              </div>
              <h3 class="avx-step-card__title">Understanding Project Requirements</h3>
              <p class="avx-step-card__desc">
                We study the client's infrastructure needs, project scope, technical requirements and operational expectations.
              </p>
            </div>
            <div class="avx-step-card__footer">
              <span class="avx-step-card__tag">
                <svg class="avx-step-card__tag-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span>Needs Assessment</span>
              </span>
            </div>
          </article>

          <!-- Step 02 -->
          <article class="avx-step-card" role="listitem">
            <div>
              <div class="avx-step-card__top">
                <span class="avx-step-card__num-badge">02</span>
                <span class="avx-step-card__stage">Phase 02 // Engineering</span>
              </div>
              <h3 class="avx-step-card__title">Technical Coordination</h3>
              <p class="avx-step-card__desc">
                We coordinate with relevant manufacturers and technical teams to identify suitable products and solutions.
              </p>
            </div>
            <div class="avx-step-card__footer">
              <span class="avx-step-card__tag">
                <svg class="avx-step-card__tag-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span>Specification Matching</span>
              </span>
            </div>
          </article>

          <!-- Step 03 -->
          <article class="avx-step-card" role="listitem">
            <div>
              <div class="avx-step-card__top">
                <span class="avx-step-card__num-badge">03</span>
                <span class="avx-step-card__stage">Phase 03 // Sourcing</span>
              </div>
              <h3 class="avx-step-card__title">Product Selection &amp; Sourcing</h3>
              <p class="avx-step-card__desc">
                We facilitate product selection and sourcing based on approved specifications, quality requirements and project needs.
              </p>
            </div>
            <div class="avx-step-card__footer">
              <span class="avx-step-card__tag">
                <svg class="avx-step-card__tag-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span>Partner Procurement</span>
              </span>
            </div>
          </article>

          <!-- Step 04 -->
          <article class="avx-step-card" role="listitem">
            <div>
              <div class="avx-step-card__top">
                <span class="avx-step-card__num-badge">04</span>
                <span class="avx-step-card__stage">Phase 04 // Logistics</span>
              </div>
              <h3 class="avx-step-card__title">Supply &amp; Delivery Coordination</h3>
              <p class="avx-step-card__desc">
                We coordinate procurement, manufacturing schedules, dispatch and delivery to the project site.
              </p>
            </div>
            <div class="avx-step-card__footer">
              <span class="avx-step-card__tag">
                <svg class="avx-step-card__tag-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span>Site Dispatch &amp; Schedule</span>
              </span>
            </div>
          </article>

          <!-- Step 05 -->
          <article class="avx-step-card" role="listitem">
            <div>
              <div class="avx-step-card__top">
                <span class="avx-step-card__num-badge">05</span>
                <span class="avx-step-card__stage">Phase 05 // Site Execution</span>
              </div>
              <h3 class="avx-step-card__title">Installation &amp; Commissioning Coordination</h3>
              <p class="avx-step-card__desc">
                We coordinate with the relevant installation teams and manufacturers for installation, testing and commissioning as applicable to the project.
              </p>
            </div>
            <div class="avx-step-card__footer">
              <span class="avx-step-card__tag">
                <svg class="avx-step-card__tag-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span>Testing &amp; Commissioning</span>
              </span>
            </div>
          </article>

          <!-- Step 06 -->
          <article class="avx-step-card" role="listitem">
            <div>
              <div class="avx-step-card__top">
                <span class="avx-step-card__num-badge">06</span>
                <span class="avx-step-card__stage">Phase 06 // Closeout</span>
              </div>
              <h3 class="avx-step-card__title">Documentation &amp; Handover Support</h3>
              <p class="avx-step-card__desc">
                We coordinate relevant product documents, test reports, warranty details and project handover documentation.
              </p>
            </div>
            <div class="avx-step-card__footer">
              <span class="avx-step-card__tag">
                <svg class="avx-step-card__tag-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                <span>Warranty &amp; Handover</span>
              </span>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- ======================================================================
         SECTION 07: QUALITY ASSURANCE (Section 4.7)
         ====================================================================== -->
    <section class="avx-quality" id="quality" aria-label="Quality Assurance">
      <div class="avx-quality__bg-grid" aria-hidden="true"></div>

      <div class="avx-container avx-quality__container">
        <div class="avx-quality__header">
          <div class="avx-quality__eyebrow avx-eyebrow">
            <span>Quality Assurance</span>
          </div>

          <h2 class="avx-quality__title">
            Quality Is Not an Option. <span class="avx-quality__title-accent">It Is a Responsibility.</span>
          </h2>

          <p class="avx-quality__intro">
            At Avenrix, we understand that healthcare infrastructure demands careful product selection, technical suitability and reliable execution. Our quality-focused approach emphasizes:
          </p>

          <div class="avx-quality__accent-rule" aria-hidden="true"></div>
        </div>

        <div class="avx-quality__layout">
          <!-- Left Column: 7 Quality Framework Points -->
          <div class="avx-quality__framework">
            <h3 class="avx-quality__framework-title">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              <span>Quality Assurance Framework</span>
            </h3>

            <ul class="avx-quality__list" role="list">
              <li class="avx-quality__item">
                <span class="avx-quality__item-icon" aria-hidden="true">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                </span>
                <span>Selection of suitable manufacturing partners.</span>
              </li>
              <li class="avx-quality__item">
                <span class="avx-quality__item-icon" aria-hidden="true">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                </span>
                <span>Verification of technical specifications.</span>
              </li>
              <li class="avx-quality__item">
                <span class="avx-quality__item-icon" aria-hidden="true">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                </span>
                <span>Coordination of pre-dispatch inspection and testing documentation, wherever applicable.</span>
              </li>
              <li class="avx-quality__item">
                <span class="avx-quality__item-icon" aria-hidden="true">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                </span>
                <span>Review of relevant product certifications and compliance documents.</span>
              </li>
              <li class="avx-quality__item">
                <span class="avx-quality__item-icon" aria-hidden="true">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                </span>
                <span>Coordination of installation and commissioning.</span>
              </li>
              <li class="avx-quality__item">
                <span class="avx-quality__item-icon" aria-hidden="true">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                </span>
                <span>Documentation and warranty coordination.</span>
              </li>
              <li class="avx-quality__item">
                <span class="avx-quality__item-icon" aria-hidden="true">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
                </span>
                <span>Attention to manufacturing quality and product reliability.</span>
              </li>
            </ul>
          </div>

          <!-- Right Column: Our Commitment & Compliance Callout Box -->
          <div class="avx-quality__cards">
            <!-- Our Commitment Card -->
            <div class="avx-quality__commitment-card">
              <span class="avx-quality__commitment-badge">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                <span>Our Quality Commitment</span>
              </span>
              <h3 class="avx-quality__commitment-title">Meeting Established Project Specs</h3>
              <p class="avx-quality__commitment-text">
                We aim to ensure that every product supplied meets the agreed specifications and the quality requirements established for the project.
              </p>
            </div>

            <!-- Compliance & Claims Control Callout -->
            <div class="avx-quality__compliance-box">
              <div class="avx-quality__compliance-header">
                <svg class="avx-quality__compliance-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
                <h4 class="avx-quality__compliance-title">Compliance &amp; Claims Control</h4>
              </div>
              <p class="avx-quality__compliance-text">
                Product certifications, test reports and compliance documents are coordinated based on verified partner documentation. NABH accreditation applies to healthcare organizations; Avenrix supports healthcare facilities in meeting relevant infrastructure and technical planning requirements.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

html = re.sub(
    r'(\s*<\/section>\s*<!-- =+\s*SECTION 05: WHY CHOOSE AVENRIX)',
    f'\n{approach_and_quality}\n    <!-- ======================================================================\n         SECTION 08: WHY CHOOSE AVENRIX',
    html
)

print("Section 06 (Approach) and Section 07 (Quality) injected.")

# -----------------------------------------------------------------------------
# 10. Update Section 08: Why Choose Avenrix (#why-avenrix) - Section 4.8 of Brief
# Update 6 Pillars to exact approved copy
# -----------------------------------------------------------------------------
why_avenrix_editorial = """          <!-- Right Column: The 6 Editorial Pillars on a Continuous Architectural Spine -->
          <div class="avx-values__editorial">
            <div class="avx-values__list">

              <!-- Value 01: Comprehensive Product Portfolio -->
              <article class="avx-value is-active" data-value-index="1" data-value-title="Comprehensive Product Portfolio" tabindex="0" aria-labelledby="val-title-01">
                <div class="avx-value__axis" aria-hidden="true">
                  <div class="avx-value__badge">
                    <span class="avx-value__number">01</span>
                    <span class="avx-value__badge-glow"></span>
                  </div>
                  <div class="avx-value__spine">
                    <div class="avx-value__spine-progress"></div>
                  </div>
                </div>

                <div class="avx-value__main">
                  <div class="avx-value__heading-wrap">
                    <div class="avx-value__connector" aria-hidden="true"></div>
                    <h3 class="avx-value__title" id="val-title-01">Comprehensive Product Portfolio</h3>
                    <span class="avx-value__tag" aria-hidden="true">Pillar 01</span>
                  </div>
                  <p class="avx-value__description">
                    Access multiple healthcare infrastructure product categories through one coordinated platform.
                  </p>
                </div>
              </article>

              <!-- Value 02: Specialized Manufacturing Network -->
              <article class="avx-value" data-value-index="2" data-value-title="Specialized Manufacturing Network" tabindex="0" aria-labelledby="val-title-02">
                <div class="avx-value__axis" aria-hidden="true">
                  <div class="avx-value__badge">
                    <span class="avx-value__number">02</span>
                    <span class="avx-value__badge-glow"></span>
                  </div>
                  <div class="avx-value__spine">
                    <div class="avx-value__spine-progress"></div>
                  </div>
                </div>

                <div class="avx-value__main">
                  <div class="avx-value__heading-wrap">
                    <div class="avx-value__connector" aria-hidden="true"></div>
                    <h3 class="avx-value__title" id="val-title-02">Specialized Manufacturing Network</h3>
                    <span class="avx-value__tag" aria-hidden="true">Pillar 02</span>
                  </div>
                  <p class="avx-value__description">
                    We work towards building relationships with specialized manufacturers and suppliers to meet diverse project requirements.
                  </p>
                </div>
              </article>

              <!-- Value 03: Project-Focused Approach -->
              <article class="avx-value" data-value-index="3" data-value-title="Project-Focused Approach" tabindex="0" aria-labelledby="val-title-03">
                <div class="avx-value__axis" aria-hidden="true">
                  <div class="avx-value__badge">
                    <span class="avx-value__number">03</span>
                    <span class="avx-value__badge-glow"></span>
                  </div>
                  <div class="avx-value__spine">
                    <div class="avx-value__spine-progress"></div>
                  </div>
                </div>

                <div class="avx-value__main">
                  <div class="avx-value__heading-wrap">
                    <div class="avx-value__connector" aria-hidden="true"></div>
                    <h3 class="avx-value__title" id="val-title-03">Project-Focused Approach</h3>
                    <span class="avx-value__tag" aria-hidden="true">Pillar 03</span>
                  </div>
                  <p class="avx-value__description">
                    Every project is approached with attention to its technical scope, specifications and operational requirements.
                  </p>
                </div>
              </article>

              <!-- Value 04: Coordinated Execution -->
              <article class="avx-value" data-value-index="4" data-value-title="Coordinated Execution" tabindex="0" aria-labelledby="val-title-04">
                <div class="avx-value__axis" aria-hidden="true">
                  <div class="avx-value__badge">
                    <span class="avx-value__number">04</span>
                    <span class="avx-value__badge-glow"></span>
                  </div>
                  <div class="avx-value__spine">
                    <div class="avx-value__spine-progress"></div>
                  </div>
                </div>

                <div class="avx-value__main">
                  <div class="avx-value__heading-wrap">
                    <div class="avx-value__connector" aria-hidden="true"></div>
                    <h3 class="avx-value__title" id="val-title-04">Coordinated Execution</h3>
                    <span class="avx-value__tag" aria-hidden="true">Pillar 04</span>
                  </div>
                  <p class="avx-value__description">
                    From sourcing and supply to installation and commissioning coordination, we aim to simplify project execution.
                  </p>
                </div>
              </article>

              <!-- Value 05: Quality-Driven Philosophy -->
              <article class="avx-value" data-value-index="5" data-value-title="Quality-Driven Philosophy" tabindex="0" aria-labelledby="val-title-05">
                <div class="avx-value__axis" aria-hidden="true">
                  <div class="avx-value__badge">
                    <span class="avx-value__number">05</span>
                    <span class="avx-value__badge-glow"></span>
                  </div>
                  <div class="avx-value__spine">
                    <div class="avx-value__spine-progress"></div>
                  </div>
                </div>

                <div class="avx-value__main">
                  <div class="avx-value__heading-wrap">
                    <div class="avx-value__connector" aria-hidden="true"></div>
                    <h3 class="avx-value__title" id="val-title-05">Quality-Driven Philosophy</h3>
                    <span class="avx-value__tag" aria-hidden="true">Pillar 05</span>
                  </div>
                  <p class="avx-value__description">
                    We emphasize suitable product selection, technical documentation and quality expectations.
                  </p>
                </div>
              </article>

              <!-- Value 06: Long-Term Relationships -->
              <article class="avx-value" data-value-index="6" data-value-title="Long-Term Relationships" tabindex="0" aria-labelledby="val-title-06">
                <div class="avx-value__axis" aria-hidden="true">
                  <div class="avx-value__badge">
                    <span class="avx-value__number">06</span>
                    <span class="avx-value__badge-glow"></span>
                  </div>
                  <div class="avx-value__spine">
                    <div class="avx-value__spine-progress"></div>
                  </div>
                </div>

                <div class="avx-value__main">
                  <div class="avx-value__heading-wrap">
                    <div class="avx-value__connector" aria-hidden="true"></div>
                    <h3 class="avx-value__title" id="val-title-06">Long-Term Relationships</h3>
                    <span class="avx-value__tag" aria-hidden="true">Pillar 06</span>
                  </div>
                  <p class="avx-value__description">
                    We believe in transparent communication, dependable coordination and lasting professional relationships.
                  </p>
                </div>
              </article>

            </div>
          </div>"""

html = re.sub(
    r'          <!-- Right Column: The 6 Editorial Pillars.*?<\/div>\s*<\/div>\s*<\/div>\s*<\/section>',
    f'{why_avenrix_editorial}\n        </div>\n      </div>\n    </section>',
    html,
    flags=re.DOTALL
)

print("Section 08 (Why Choose Avenrix) updated.")

# -----------------------------------------------------------------------------
# 11. Inject Section 09: Manufacturing & Supply Partnerships (#partnerships)
# AND Section 10: Frequently Asked Questions (#faqs)
# (Injected immediately after #why-avenrix and before #contact)
# -----------------------------------------------------------------------------
partnerships_and_faqs = """    <!-- ======================================================================
         SECTION 09: MANUFACTURING & SUPPLY PARTNERSHIPS (Section 4.9)
         ====================================================================== -->
    <section class="avx-partnerships" id="partnerships" aria-label="Manufacturing & Supply Partnerships">
      <div class="avx-partnerships__bg-grid" aria-hidden="true"></div>

      <div class="avx-container avx-partnerships__container">
        <div class="avx-partnerships__header">
          <div class="avx-partnerships__eyebrow avx-eyebrow">
            <span>Partnership Model</span>
          </div>

          <h2 class="avx-partnerships__title">
            Connecting Specialized Manufacturing with <span class="avx-partnerships__title-accent">Healthcare Infrastructure Needs</span>
          </h2>

          <div class="avx-partnerships__accent-rule" aria-hidden="true"></div>
        </div>

        <!-- Partnership Narrative Cards -->
        <div class="avx-partnerships__intro-grid">
          <div class="avx-partnerships__intro-card">
            <span class="avx-partnerships__intro-label">Collaboration Platform</span>
            <p class="avx-partnerships__intro-text">
              Avenrix operates through a manufacturing and supply partnership model, bringing together specialized manufacturers, suppliers and project requirements.
            </p>
          </div>
          <div class="avx-partnerships__intro-card">
            <span class="avx-partnerships__intro-label">Technical Coordination</span>
            <p class="avx-partnerships__intro-text">
              We focus on identifying suitable products, coordinating technical specifications, facilitating procurement and supporting delivery and project execution.
            </p>
          </div>
          <div class="avx-partnerships__intro-card">
            <span class="avx-partnerships__intro-label">Agile Scalability</span>
            <p class="avx-partnerships__intro-text">
              Our model enables us to address diverse infrastructure requirements without limiting our offerings to products manufactured in-house.
            </p>
          </div>
        </div>

        <!-- 5 Partnership Philosophy Pillars -->
        <div class="avx-partnerships__pillars-wrap">
          <h3 class="avx-partnerships__pillars-heading">Our Partnership Philosophy</h3>
          <div class="avx-partnerships__pillars-grid" role="list">
            <div class="avx-pillar-card" role="listitem">
              <span class="avx-pillar-card__num">01 // RELATIONSHIPS</span>
              <p class="avx-pillar-card__text">Professional manufacturer relationships.</p>
            </div>
            <div class="avx-pillar-card" role="listitem">
              <span class="avx-pillar-card__num">02 // COORDINATION</span>
              <p class="avx-pillar-card__text">Clear technical and commercial coordination.</p>
            </div>
            <div class="avx-pillar-card" role="listitem">
              <span class="avx-pillar-card__num">03 // EXPECTATIONS</span>
              <p class="avx-pillar-card__text">Agreed quality and delivery expectations.</p>
            </div>
            <div class="avx-pillar-card" role="listitem">
              <span class="avx-pillar-card__num">04 // TRANSPARENCY</span>
              <p class="avx-pillar-card__text">Transparent communication.</p>
            </div>
            <div class="avx-pillar-card" role="listitem">
              <span class="avx-pillar-card__num">05 // COLLABORATION</span>
              <p class="avx-pillar-card__text">Long-term business collaboration.</p>
            </div>
          </div>
        </div>

        <!-- For Manufacturers CTA Card -->
        <div class="avx-partnerships__mfg-banner">
          <div class="avx-partnerships__mfg-content">
            <span class="avx-partnerships__mfg-badge">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="23" y1="11" x2="17" y2="11"/></svg>
              <span>For Equipment &amp; Component Manufacturers</span>
            </span>
            <h3 class="avx-partnerships__mfg-title">Partner With Avenrix</h3>
            <p class="avx-partnerships__mfg-desc">
              Are you a manufacturer of AHU systems, modular OT equipment, MGPS, cleanroom products or specialized medical equipment? We welcome opportunities to explore manufacturing, dealership and supply partnerships.
            </p>
          </div>
          <div class="avx-partnerships__mfg-cta">
            <a href="#contact" class="avx-btn avx-btn--primary avx-partnerships__btn">
              <span>Become an Avenrix Manufacturing Partner</span>
              <svg class="avx-icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
                <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- ======================================================================
         SECTION 10: FREQUENTLY ASKED QUESTIONS (Section 4.10)
         ====================================================================== -->
    <section class="avx-faqs" id="faqs" aria-label="Frequently Asked Questions">
      <div class="avx-faqs__bg-grid" aria-hidden="true"></div>

      <div class="avx-container avx-faqs__container">
        <div class="avx-faqs__header">
          <div class="avx-faqs__eyebrow avx-eyebrow">
            <span>Common Questions</span>
          </div>

          <h2 class="avx-faqs__title">
            Frequently Asked <span class="avx-faqs__title-accent">Questions</span>
          </h2>

          <p class="avx-faqs__intro">
            Clear information about our turnkey healthcare infrastructure coordination, partnership model and project execution.
          </p>

          <div class="avx-faqs__accent-rule" aria-hidden="true"></div>
        </div>

        <div class="avx-faqs__accordion" role="region" aria-label="Avenrix FAQs Accordion">
          <!-- FAQ 01 -->
          <div class="avx-faq-item is-open">
            <button type="button" class="avx-faq-trigger" aria-expanded="true">
              <span class="avx-faq-question">What does Avenrix Healthcare Solutions provide?</span>
              <span class="avx-faq-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
              </span>
            </button>
            <div class="avx-faq-panel">
              <p class="avx-faq-answer">
                Avenrix provides healthcare and pharmaceutical infrastructure solutions, including HVAC, AHU, modular operation theatres, MGPS, cleanroom systems, modular panels and specialized medical equipment.
              </p>
            </div>
          </div>

          <!-- FAQ 02 -->
          <div class="avx-faq-item">
            <button type="button" class="avx-faq-trigger" aria-expanded="false">
              <span class="avx-faq-question">Does Avenrix manufacture its own products?</span>
              <span class="avx-faq-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
              </span>
            </button>
            <div class="avx-faq-panel">
              <p class="avx-faq-answer">
                Avenrix follows a manufacturing and supply partnership model, sourcing products through specialized manufacturers and suppliers.
              </p>
            </div>
          </div>

          <!-- FAQ 03 -->
          <div class="avx-faq-item">
            <button type="button" class="avx-faq-trigger" aria-expanded="false">
              <span class="avx-faq-question">Does Avenrix provide turnkey solutions?</span>
              <span class="avx-faq-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
              </span>
            </button>
            <div class="avx-faq-panel">
              <p class="avx-faq-answer">
                Avenrix aims to coordinate complete project requirements, including product sourcing, supply, installation coordination, commissioning support and documentation, depending on the agreed project scope.
              </p>
            </div>
          </div>

          <!-- FAQ 04 -->
          <div class="avx-faq-item">
            <button type="button" class="avx-faq-trigger" aria-expanded="false">
              <span class="avx-faq-question">Does Avenrix work with architects and consultants?</span>
              <span class="avx-faq-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
              </span>
            </button>
            <div class="avx-faq-panel">
              <p class="avx-faq-answer">
                Yes. We welcome collaboration with architects, healthcare consultants, project management consultants, contractors and EPC companies.
              </p>
            </div>
          </div>

          <!-- FAQ 05 -->
          <div class="avx-faq-item">
            <button type="button" class="avx-faq-trigger" aria-expanded="false">
              <span class="avx-faq-question">Can customers request customized solutions?</span>
              <span class="avx-faq-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
              </span>
            </button>
            <div class="avx-faq-panel">
              <p class="avx-faq-answer">
                Yes. Solutions can be evaluated according to project requirements, technical specifications and available manufacturing capabilities.
              </p>
            </div>
          </div>

          <!-- FAQ 06 -->
          <div class="avx-faq-item">
            <button type="button" class="avx-faq-trigger" aria-expanded="false">
              <span class="avx-faq-question">Does Avenrix work with government projects?</span>
              <span class="avx-faq-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
              </span>
            </button>
            <div class="avx-faq-panel">
              <p class="avx-faq-answer">
                Avenrix can explore government healthcare infrastructure projects and procurement opportunities subject to applicable eligibility, tender conditions and documentation requirements.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

html = re.sub(
    r'(\s*<!-- =+\s*SECTION 06: CONTACT US)',
    f'\n{partnerships_and_faqs}\n    <!-- ======================================================================\n         SECTION 11: CONTACT US',
    html
)

print("Section 09 (Partnerships) and Section 10 (FAQs) injected.")

# -----------------------------------------------------------------------------
# 12. Update Section 11: Contact Us (#contact) - Section 4.11 of Brief
# Update Headline, Copy, Form Fields (Designation, Location, Requirement Type)
# -----------------------------------------------------------------------------
contact_headline_old = """            <h2 class="avx-contact__title" id="contact-heading">
              Let’s Discuss <span class="avx-contact__title-accent">Your Project</span>
            </h2>
            <div class="avx-contact__accent-rule" aria-hidden="true"></div>
            <p class="avx-contact__lead">
              Planning a new healthcare facility, upgrading existing infrastructure, or need specialized equipment? Talk to our solutions team today.
            </p>
            <p class="avx-contact__desc">
              Whether you are an architect, hospital director, biomedical engineer, or project consultant, our specialists are ready to collaborate.
            </p>"""

contact_headline_new = """            <h2 class="avx-contact__title" id="contact-heading">
              Let's Build Better <span class="avx-contact__title-accent">Healthcare Infrastructure Together.</span>
            </h2>
            <div class="avx-contact__accent-rule" aria-hidden="true"></div>
            <p class="avx-contact__lead">
              Whether you are planning a new hospital, upgrading an existing healthcare facility, developing a pharmaceutical cleanroom or looking for specialized medical equipment, Avenrix is ready to understand your requirements.
            </p>
            <p class="avx-contact__desc">
              Connect with our team to discuss your next project.
            </p>"""

if contact_headline_old in html:
    html = html.replace(contact_headline_old, contact_headline_new)

# Update Form Fields in #contact
old_form = """            <!-- Client Enquiry Form -->
            <form class="avx-contact__form" id="avxContactForm" novalidate>
              <div class="avx-contact__row avx-contact__row--two-col">
                <!-- Name (Required) -->
                <div class="avx-contact__field" id="fieldWrapName">
                  <label for="avxContactName" class="avx-contact__label">
                    <span>Full Name</span>
                    <span class="avx-contact__required" aria-hidden="true">*</span>
                  </label>
                  <input 
                    type="text" 
                    id="avxContactName" 
                    name="name" 
                    class="avx-contact__input" 
                    placeholder="e.g. Dr. Rajesh Sharma"
                    autocomplete="name"
                    required
                    aria-required="true"
                    aria-describedby="avxNameError"
                  >
                  <div class="avx-contact__error" id="avxNameError" role="alert" aria-live="polite"></div>
                </div>

                <!-- Company (Optional) -->
                <div class="avx-contact__field" id="fieldWrapCompany">
                  <label for="avxContactCompany" class="avx-contact__label">
                    <span>Hospital / Organization</span>
                    <span class="avx-contact__optional">(optional)</span>
                  </label>
                  <input 
                    type="text" 
                    id="avxContactCompany" 
                    name="company" 
                    class="avx-contact__input" 
                    placeholder="e.g. Apollo Health City"
                    autocomplete="organization"
                  >
                </div>
              </div>

              <div class="avx-contact__row avx-contact__row--two-col">
                <!-- Email (Required) -->
                <div class="avx-contact__field" id="fieldWrapEmail">
                  <label for="avxContactEmail" class="avx-contact__label">
                    <span>Email Address</span>
                    <span class="avx-contact__required" aria-hidden="true">*</span>
                  </label>
                  <input 
                    type="email" 
                    id="avxContactEmail" 
                    name="email" 
                    class="avx-contact__input" 
                    placeholder="e.g. rajesh@hospital.com"
                    autocomplete="email"
                    required
                    aria-required="true"
                    aria-describedby="avxEmailError"
                  >
                  <div class="avx-contact__error" id="avxEmailError" role="alert" aria-live="polite"></div>
                </div>

                <!-- Phone (Required) -->
                <div class="avx-contact__field" id="fieldWrapPhone">
                  <label for="avxContactPhone" class="avx-contact__label">
                    <span>Phone Number</span>
                    <span class="avx-contact__required" aria-hidden="true">*</span>
                  </label>
                  <input 
                    type="tel" 
                    id="avxContactPhone" 
                    name="phone" 
                    class="avx-contact__input" 
                    placeholder="e.g. +91 98765 43210"
                    autocomplete="tel"
                    required
                    aria-required="true"
                    aria-describedby="avxPhoneError"
                  >
                  <div class="avx-contact__error" id="avxPhoneError" role="alert" aria-live="polite"></div>
                </div>
              </div>

              <!-- Product / Service Interest (Optional Select) -->
              <div class="avx-contact__field" id="fieldWrapProduct">
                <label for="avxContactProduct" class="avx-contact__label">
                  <span>Interested Solution / Product</span>
                  <span class="avx-contact__optional">(optional)</span>
                </label>
                <select id="avxContactProduct" name="product" class="avx-contact__select">
                  <option value="">Select a solution or product</option>
                  <option value="HVAC &amp; AHU Systems">HVAC &amp; AHU Systems</option>
                  <option value="Modular Operation Theatres">Modular Operation Theatres (OT)</option>
                  <option value="Modular Wall &amp; Ceiling Systems">Modular Wall &amp; Ceiling Systems</option>
                  <option value="Medical Gas Pipeline Systems">Medical Gas Pipeline Systems (MGPS)</option>
                  <option value="Medical Equipment &amp; Accessories">Medical Equipment &amp; Accessories</option>
                  <option value="Cleanroom &amp; Pharmaceutical Infrastructure">Cleanroom &amp; Pharmaceutical Infrastructure</option>
                  <option value="Turnkey Project Solutions">Turnkey Project Solutions</option>
                </select>
              </div>

              <!-- Message (Optional Textarea) -->
              <div class="avx-contact__field" id="fieldWrapMessage">
                <label for="avxContactMessage" class="avx-contact__label">
                  <span>Project Scope / Message</span>
                  <span class="avx-contact__optional">(optional)</span>
                </label>
                <textarea 
                  id="avxContactMessage" 
                  name="message" 
                  class="avx-contact__textarea" 
                  rows="2" 
                  placeholder="Outline your facility requirements, scope, timeline, or specific inquiries..."
                ></textarea>
              </div>

              <!-- Submit Button -->
              <div class="avx-contact__submit-wrap">
                <button type="submit" class="avx-contact__submit" id="avxContactSubmit">
                  <span class="avx-contact__submit-text">Submit Inquiry</span>
                  <svg class="avx-contact__arrow" viewBox="0 0 16 16" fill="none" aria-hidden="true">
                    <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
                <div class="avx-contact__form-alert" id="avxContactAlert" role="alert" aria-live="assertive"></div>
              </div>
            </form>"""

new_form = """            <!-- Client Enquiry Form (Section 4.11 Form Fields) -->
            <form class="avx-contact__form" id="avxContactForm" novalidate>
              <div class="avx-contact__row avx-contact__row--two-col">
                <!-- Name (Required) -->
                <div class="avx-contact__field" id="fieldWrapName">
                  <label for="avxContactName" class="avx-contact__label">
                    <span>Full Name</span>
                    <span class="avx-contact__required" aria-hidden="true">*</span>
                  </label>
                  <input 
                    type="text" 
                    id="avxContactName" 
                    name="name" 
                    class="avx-contact__input" 
                    placeholder="e.g. Dr. Rajesh Sharma"
                    autocomplete="name"
                    required
                    aria-required="true"
                    aria-describedby="avxNameError"
                  >
                  <div class="avx-contact__error" id="avxNameError" role="alert" aria-live="polite"></div>
                </div>

                <!-- Company / Organization -->
                <div class="avx-contact__field" id="fieldWrapCompany">
                  <label for="avxContactCompany" class="avx-contact__label">
                    <span>Company / Organization</span>
                    <span class="avx-contact__optional">(optional)</span>
                  </label>
                  <input 
                    type="text" 
                    id="avxContactCompany" 
                    name="company" 
                    class="avx-contact__input" 
                    placeholder="e.g. Apollo Healthcare / Cleanroom facility"
                    autocomplete="organization"
                  >
                </div>
              </div>

              <div class="avx-contact__row avx-contact__row--two-col">
                <!-- Designation -->
                <div class="avx-contact__field" id="fieldWrapDesignation">
                  <label for="avxContactDesignation" class="avx-contact__label">
                    <span>Designation</span>
                    <span class="avx-contact__optional">(optional)</span>
                  </label>
                  <input 
                    type="text" 
                    id="avxContactDesignation" 
                    name="designation" 
                    class="avx-contact__input" 
                    placeholder="e.g. Medical Director / Project Engineer / Architect"
                  >
                </div>

                <!-- Project Location -->
                <div class="avx-contact__field" id="fieldWrapLocation">
                  <label for="avxContactLocation" class="avx-contact__label">
                    <span>Project Location</span>
                    <span class="avx-contact__optional">(optional)</span>
                  </label>
                  <input 
                    type="text" 
                    id="avxContactLocation" 
                    name="location" 
                    class="avx-contact__input" 
                    placeholder="e.g. Hyderabad, Telangana"
                  >
                </div>
              </div>

              <div class="avx-contact__row avx-contact__row--two-col">
                <!-- Email (Required) -->
                <div class="avx-contact__field" id="fieldWrapEmail">
                  <label for="avxContactEmail" class="avx-contact__label">
                    <span>Email Address</span>
                    <span class="avx-contact__required" aria-hidden="true">*</span>
                  </label>
                  <input 
                    type="email" 
                    id="avxContactEmail" 
                    name="email" 
                    class="avx-contact__input" 
                    placeholder="e.g. rajesh@hospital.com"
                    autocomplete="email"
                    required
                    aria-required="true"
                    aria-describedby="avxEmailError"
                  >
                  <div class="avx-contact__error" id="avxEmailError" role="alert" aria-live="polite"></div>
                </div>

                <!-- Contact Number (Required) -->
                <div class="avx-contact__field" id="fieldWrapPhone">
                  <label for="avxContactPhone" class="avx-contact__label">
                    <span>Contact Number</span>
                    <span class="avx-contact__required" aria-hidden="true">*</span>
                  </label>
                  <input 
                    type="tel" 
                    id="avxContactPhone" 
                    name="phone" 
                    class="avx-contact__input" 
                    placeholder="e.g. +91 98765 43210"
                    autocomplete="tel"
                    required
                    aria-required="true"
                    aria-describedby="avxPhoneError"
                  >
                  <div class="avx-contact__error" id="avxPhoneError" role="alert" aria-live="polite"></div>
                </div>
              </div>

              <div class="avx-contact__row avx-contact__row--two-col">
                <!-- Type of Requirement (Dropdown) -->
                <div class="avx-contact__field" id="fieldWrapReqType">
                  <label for="avxContactReqType" class="avx-contact__label">
                    <span>Type of Requirement</span>
                    <span class="avx-contact__optional">(optional)</span>
                  </label>
                  <select id="avxContactReqType" name="requirementType" class="avx-contact__select">
                    <option value="">Select requirement type</option>
                    <option value="New Healthcare Project">New Healthcare Project</option>
                    <option value="Facility Upgrade / Renovation">Facility Upgrade / Renovation</option>
                    <option value="Product &amp; Equipment Sourcing">Product &amp; Equipment Sourcing</option>
                    <option value="Technical Consultation">Technical Consultation</option>
                    <option value="Manufacturing / Dealership Partnership">Manufacturing / Dealership Partnership</option>
                  </select>
                </div>

                <!-- Product / Solution Required -->
                <div class="avx-contact__field" id="fieldWrapProduct">
                  <label for="avxContactProduct" class="avx-contact__label">
                    <span>Product / Solution Required</span>
                    <span class="avx-contact__optional">(optional)</span>
                  </label>
                  <select id="avxContactProduct" name="product" class="avx-contact__select">
                    <option value="">Select solution or product</option>
                    <option value="HVAC &amp; AHU Solutions">HVAC &amp; AHU Solutions</option>
                    <option value="Modular Operation Theatres">Modular Operation Theatres (OT)</option>
                    <option value="Modular Wall, Ceiling &amp; Flooring">Modular Wall, Ceiling &amp; Flooring</option>
                    <option value="Medical Gas Pipeline Systems (MGPS)">Medical Gas Pipeline Systems (MGPS)</option>
                    <option value="Cleanroom &amp; Pharmaceutical Infrastructure">Cleanroom &amp; Pharmaceutical Infrastructure</option>
                    <option value="Medical Equipment &amp; Accessories">Medical Equipment &amp; Accessories</option>
                    <option value="Complete Turnkey Infrastructure Coordination">Complete Turnkey Infrastructure Coordination</option>
                  </select>
                </div>
              </div>

              <!-- Project Description (Textarea) -->
              <div class="avx-contact__field" id="fieldWrapMessage">
                <label for="avxContactMessage" class="avx-contact__label">
                  <span>Project Description</span>
                  <span class="avx-contact__optional">(optional)</span>
                </label>
                <textarea 
                  id="avxContactMessage" 
                  name="message" 
                  class="avx-contact__textarea" 
                  rows="2" 
                  placeholder="Outline your facility requirements, technical scope, timeline or specific equipment questions..."
                ></textarea>
              </div>

              <!-- Submit Button with Section 4.11 Approved CTA -->
              <div class="avx-contact__submit-wrap">
                <button type="submit" class="avx-contact__submit" id="avxContactSubmit">
                  <span class="avx-contact__submit-text">Discuss Your Project With Avenrix</span>
                  <svg class="avx-contact__arrow" viewBox="0 0 16 16" fill="none" aria-hidden="true">
                    <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
                <div class="avx-contact__form-alert" id="avxContactAlert" role="alert" aria-live="assertive"></div>
              </div>
            </form>"""

html = re.sub(
    r'            <!-- Client Enquiry Form -->.*?<\/form>',
    new_form,
    html,
    flags=re.DOTALL
)

print("Section 11 (Contact) updated.")

# -----------------------------------------------------------------------------
# 13. Update Footer Specification (Section 5 of Brief)
# -----------------------------------------------------------------------------
footer_col1_old = """          <p class="avx-footer__summary">
            <strong>Engineering Healthcare. Building Trust.</strong><br>
            Complete Healthcare Infrastructure Solutions for Hospitals, Clinics, and Pharmaceutical Facilities. Operating on a quality-driven sourcing and partner coordination model.
          </p>"""

footer_col1_new = """          <p class="avx-footer__summary">
            <strong>Engineering Healthcare. Building Trust.</strong><br>
            Complete Turnkey Healthcare &amp; Pharmaceutical Infrastructure Solutions.
          </p>"""

if footer_col1_old in html:
    html = html.replace(footer_col1_old, footer_col1_new)

# Footer Quick Links per Section 5:
# Home | About Us | Our Solutions | Products | Industries We Serve | Quality Assurance | Contact Us
footer_quick_links = """        <!-- Col 2: Quick Links (Section 5 Spec) -->
        <div>
          <h3 class="avx-footer__heading">Quick Links</h3>
          <ul class="avx-footer__list">
            <li><a href="#home" class="avx-footer__link">Home</a></li>
            <li><a href="#about" class="avx-footer__link">About Us</a></li>
            <li><a href="#solutions" class="avx-footer__link">Our Solutions</a></li>
            <li><a href="#products" class="avx-footer__link">Products</a></li>
            <li><a href="#industries" class="avx-footer__link">Industries We Serve</a></li>
            <li><a href="#quality" class="avx-footer__link">Quality Assurance</a></li>
            <li><a href="#contact" class="avx-footer__link">Contact Us</a></li>
          </ul>
        </div>"""

html = re.sub(
    r'        <!-- Col 2: Navigation Links -->.*?<\/div>',
    footer_quick_links,
    html,
    flags=re.DOTALL
)

# Footer Solution Links per Section 5:
# HVAC & AHU | Modular OT | MGPS | Cleanroom | Medical Equipment
footer_solution_links = """        <!-- Col 3: Solution Links (Section 5 Spec) -->
        <div>
          <h3 class="avx-footer__heading">Solution Links</h3>
          <ul class="avx-footer__list">
            <li><a href="#solutions" class="avx-footer__link">HVAC &amp; AHU</a></li>
            <li><a href="#solutions" class="avx-footer__link">Modular OT</a></li>
            <li><a href="#solutions" class="avx-footer__link">MGPS</a></li>
            <li><a href="#solutions" class="avx-footer__link">Cleanroom</a></li>
            <li><a href="#solutions" class="avx-footer__link">Medical Equipment</a></li>
          </ul>
        </div>"""

html = re.sub(
    r'        <!-- Col 3: Solutions Overview -->.*?<\/div>',
    footer_solution_links,
    html,
    flags=re.DOTALL
)

# Write updated HTML
with open('index.html', 'w', encoding='utf-8') as out:
    out.write(html)

print("index.html upgraded successfully and written to disk!")
