# -*- coding: utf-8 -*-
"""
Verification Script for Avenrix Healthcare Solutions Website Upgrade
Validates against all criteria in Avenrix_Antigravity_Website_Upgrade_Brief.docx
"""

import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

errors = []
successes = []

def check(condition, message):
    if condition:
        successes.append(f"PASS: {message}")
    else:
        errors.append(f"FAIL: {message}")

# 1. SEO & Title
check('Avenrix Healthcare Solutions | Turnkey Healthcare Infrastructure' in html, "Homepage Title matches Section 8")
check('Avenrix Healthcare Solutions coordinates turnkey healthcare and pharmaceutical infrastructure solutions' in html, "Homepage Meta Description matches Section 8")

# 2. Section Order
expected_sections = [
    'home', 'about', 'solutions', 'products', 'industries',
    'approach', 'quality', 'why-avenrix', 'partnerships', 'faqs', 'contact'
]
actual_sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', html)
check(actual_sections == expected_sections, f"All 11 sections in exact recommended order: {actual_sections}")

# 3. Section 01: Home
check('Engineering Healthcare. <span class="avx-hero__title-accent">Building Trust.</span>' in html, "Hero Title present")
check('Complete Turnkey Healthcare &amp; Pharmaceutical Infrastructure Solutions' in html, "Hero Subtitle present")
check('Building the Infrastructure Behind Better Healthcare' in html, "Homepage Intro headline present")
check('HVAC &amp; AHU Solutions' in html and 'Modular Operation Theatres' in html, "Highlight solution cards present")

# 4. Section 02: About
check('Avenrix Healthcare Solutions is a healthcare infrastructure solutions company focused on delivering integrated products' in html, "About Who We Are text present")
check('To become a trusted name in healthcare and pharmaceutical infrastructure' in html, "Our Vision present")
mission_points = [
    'To provide comprehensive healthcare infrastructure solutions under one platform',
    'To connect clients with specialized and dependable manufacturing partners',
    'To promote quality, technical suitability and transparency',
    'To simplify infrastructure procurement and project coordination',
    'To build long-term relationships through reliability and professional service'
]
for mp in mission_points:
    check(mp in html, f"Mission point: {mp[:40]}...")

check('ENGINEERING HEALTHCARE. BUILDING TRUST.' in html, "Philosophy exact quote present")
check('For us, this is more than a tagline' in html, "Philosophy body present")

# 5. Section 03: Our Solutions
check('Integrated Solutions for <span class="avx-solutions__title-accent">Every Healthcare Environment</span>' in html, "Solutions headline present")
check('We provide HVAC and air handling solutions for specialized healthcare environments' in html, "Solution 01 copy present")
check('We coordinate complete modular operation theatre solutions' in html, "Solution 02 copy present")
check('We supply and coordinate specialized architectural infrastructure' in html, "Solution 03 copy present")
check('We offer medical gas pipeline infrastructure solutions' in html, "Solution 04 copy present")
check('We support infrastructure requirements for pharmaceutical' in html, "Solution 05 copy present")
check('We coordinate the supply of specialized medical equipment' in html, "Solution 06 copy present")

# 6. Section 04: Products & Equipment
check('Specialized Products. Integrated Infrastructure.' in html, "Products headline present")
check('Need technical specifications, product details or pricing?' in html, "Product bottom CTA banner present")
check('Request Product Information' in html, "Product CTA button present")
check('id="ahuHvacSlider"' in html, "Dual auto-slider preserved on Card 01")

# 7. Section 05: Industries
check('Tailored Solutions for Every <span class="avx-industries__title-accent">Specialized Healthcare Environment</span>' in html, "Industries headline present")
check('id="industriesDomainLead"' in html, "Industries 3-vertical tab hub preserved")

# 8. Section 06: Our Approach (NEW)
check('From Concept to Completion:' in html, "Approach headline present")
approach_steps = [
    'Understanding Project Requirements',
    'Technical Coordination',
    'Product Selection &amp; Sourcing',
    'Supply &amp; Delivery Coordination',
    'Installation &amp; Commissioning Coordination',
    'Documentation &amp; Handover Support'
]
for st in approach_steps:
    check(st in html, f"Approach step: {st}")

# 9. Section 07: Quality Assurance (NEW)
check('Quality Is Not an Option. <span class="avx-quality__title-accent">It Is a Responsibility.</span>' in html, "Quality headline present")
check('Selection of suitable manufacturing partners.' in html, "Quality point 1 present")
check('Verification of technical specifications.' in html, "Quality point 2 present")
check('Meeting Established Project Specs' in html, "Our Quality Commitment card present")
check('Compliance &amp; Claims Control' in html, "Compliance callout box present")

# 10. Section 08: Why Choose Avenrix
why_pillars = [
    'Comprehensive Product Portfolio',
    'Specialized Manufacturing Network',
    'Project-Focused Approach',
    'Coordinated Execution',
    'Quality-Driven Philosophy',
    'Long-Term Relationships'
]
for wp in why_pillars:
    check(wp in html, f"Why Avenrix pillar: {wp}")

# 11. Section 09: Partnerships (NEW)
check('Connecting Specialized Manufacturing with' in html, "Partnerships headline present")
check('Our Partnership Philosophy' in html, "Partnership philosophy present")
check('Partner With Avenrix' in html, "For Manufacturers CTA title present")
check('Become an Avenrix Manufacturing Partner' in html, "Become Manufacturing Partner CTA button present")

# 12. Section 10: FAQs (NEW)
faq_questions = [
    'What does Avenrix Healthcare Solutions provide?',
    'Does Avenrix manufacture its own products?',
    'Does Avenrix provide turnkey solutions?',
    'Does Avenrix work with architects and consultants?',
    'Can customers request customized solutions?',
    'Does Avenrix work with government projects?'
]
for fq in faq_questions:
    check(fq in html, f"FAQ question: {fq}")

# 13. Section 11: Contact Us
check("Let's Build Better <span class=\"avx-contact__title-accent\">Healthcare Infrastructure Together.</span>" in html, "Contact headline present")
check('avenrixhealthcaresolutions@gmail.com' in html, "Verified Email present")
check('https://www.instagram.com/avenrixhealthcaresolutions' in html, "Verified Instagram link present")
check('https://www.facebook.com/share/1GcCszMUb7/' in html, "Verified Facebook link present")
check('id="avxContactDesignation"' in html, "Form field Designation present")
check('id="avxContactLocation"' in html, "Form field Project Location present")
check('id="avxContactReqType"' in html, "Form field Type of Requirement present")
check('Discuss Your Project With Avenrix' in html, "CTA Discuss Your Project With Avenrix present")

# 14. Footer
check('<strong>Engineering Healthcare. Building Trust.</strong>' in html, "Footer Tagline present")
check('Complete Turnkey Healthcare &amp; Pharmaceutical Infrastructure Solutions.' in html, "Footer Descriptor present")

# 15. Guardrails check
check('.avx-card__corner' not in html and 'avx-solution-card__corner' not in html and 'avx-industry-card__corner' not in html, "No corner crosshairs (+) present")

# 16. Google Sheets Integration check in js/main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

check('AKfycbyhVG4olpXlaZCqQNtyx7s-8DW1u1GK2Ol3OqXT9lsG8xpbtSf8UqM0SYPS9TVjdSTt' in js, "Google Sheets Web App ID intact in js/main.js")
check('designation: designationInput' in js, "Designation payload in js/main.js")
check('location: locationInput' in js, "Location payload in js/main.js")
check('requirementType: reqTypeSelect' in js, "RequirementType payload in js/main.js")
check('initFaqAccordion' in js, "initFaqAccordion in js/main.js")

print(f"\nTotal Checks: {len(successes) + len(errors)}")
print(f"Passed: {len(successes)}")
print(f"Failed: {len(errors)}")

if errors:
    print("\nERRORS:")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)
else:
    print("\nALL UPGRADE SPEC CHECKS PASSED PERFECTLY!")
