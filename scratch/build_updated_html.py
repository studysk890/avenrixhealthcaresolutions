# -*- coding: utf-8 -*-
"""
Script to construct the upgraded index.html for Avenrix Healthcare Solutions.
"""

# Read the original HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Title and Meta Description
old_title_meta = """    <title>Avenrix Healthcare Solutions — Engineering Healthcare. Building Trust.</title>
    <meta name="description" content="Avenrix Healthcare Solutions — Complete healthcare infrastructure solutions for hospitals, clinics, and pharmaceutical facilities. Sourcing and solution coordination.">"""

new_title_meta = """    <title>Avenrix Healthcare Solutions | Turnkey Healthcare Infrastructure</title>
    <meta name="description" content="Avenrix Healthcare Solutions coordinates turnkey healthcare and pharmaceutical infrastructure solutions, including HVAC, modular OT, MGPS, cleanroom systems and medical equipment.">"""

assert old_title_meta in html, "Failed to match old_title_meta"
html = html.replace(old_title_meta, new_title_meta)

# 2. Add New Modular Stylesheets in <head>
old_css_links = """  <link rel="stylesheet" href="css/products.css">
  <link rel="stylesheet" href="css/industries.css">
  <link rel="stylesheet" href="css/values.css">
  <link rel="stylesheet" href="css/contact.css">
  <link rel="stylesheet" href="css/footer.css">"""

new_css_links = """  <link rel="stylesheet" href="css/products.css">
  <link rel="stylesheet" href="css/industries.css">
  <link rel="stylesheet" href="css/approach.css">
  <link rel="stylesheet" href="css/quality.css">
  <link rel="stylesheet" href="css/values.css">
  <link rel="stylesheet" href="css/partnerships.css">
  <link rel="stylesheet" href="css/faqs.css">
  <link rel="stylesheet" href="css/contact.css">
  <link rel="stylesheet" href="css/footer.css">"""

assert old_css_links in html, "Failed to match old_css_links"
html = html.replace(old_css_links, new_css_links)

# 3. Update Desktop Navigation and Mobile Drawer
old_nav = """      <!-- Desktop Navigation Menu (Proposal 7-Item Navigation) -->
      <nav class="avx-header__nav" aria-label="Primary Navigation">
        <ul class="avx-header__nav-list">
          <li class="avx-header__nav-item">
            <a href="#home" class="avx-header__nav-link is-active">Home</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#about" class="avx-header__nav-link">About Us</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#solutions" class="avx-header__nav-link">Solutions</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#products" class="avx-header__nav-link">Products</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#industries" class="avx-header__nav-link">Industries</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#why-avenrix" class="avx-header__nav-link">Why Avenrix</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#contact" class="avx-header__nav-link">Contact</a>
          </li>
        </ul>
      </nav>"""

new_nav = """      <!-- Desktop Navigation Menu -->
      <nav class="avx-header__nav" aria-label="Primary Navigation">
        <ul class="avx-header__nav-list">
          <li class="avx-header__nav-item">
            <a href="#about" class="avx-header__nav-link">About Us</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#solutions" class="avx-header__nav-link">Solutions</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#products" class="avx-header__nav-link">Products</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#industries" class="avx-header__nav-link">Industries</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#approach" class="avx-header__nav-link">Approach</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#quality" class="avx-header__nav-link">Quality</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#why-avenrix" class="avx-header__nav-link">Why Avenrix</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#faqs" class="avx-header__nav-link">FAQs</a>
          </li>
          <li class="avx-header__nav-item">
            <a href="#contact" class="avx-header__nav-link">Contact</a>
          </li>
        </ul>
      </nav>"""

assert old_nav in html, "Failed to match old_nav"
html = html.replace(old_nav, new_nav)

old_drawer = """      <ul class="avx-drawer__list">
        <li class="avx-drawer__item"><a href="#home" class="avx-drawer__link is-active">Home</a></li>
        <li class="avx-drawer__item"><a href="#about" class="avx-drawer__link">About Us</a></li>
        <li class="avx-drawer__item"><a href="#solutions" class="avx-drawer__link">Our Solutions</a></li>
        <li class="avx-drawer__item"><a href="#products" class="avx-drawer__link">Products</a></li>
        <li class="avx-drawer__item"><a href="#industries" class="avx-drawer__link">Industries</a></li>
        <li class="avx-drawer__item"><a href="#why-avenrix" class="avx-drawer__link">Why Avenrix</a></li>
        <li class="avx-drawer__item"><a href="#contact" class="avx-drawer__link">Contact Us</a></li>
      </ul>"""

new_drawer = """      <ul class="avx-drawer__list">
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

assert old_drawer in html, "Failed to match old_drawer"
html = html.replace(old_drawer, new_drawer)

print("Steps 1, 2, and 3 matched and replaced successfully.")

with open('scratch/temp_part1.html', 'w', encoding='utf-8') as out:
    out.write(html)
