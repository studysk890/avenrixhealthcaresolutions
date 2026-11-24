from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1440,900")

driver = webdriver.Chrome(options=options)
url = "file:///" + os.path.abspath("index.html").replace("\\", "/")
print("Loading:", url)
driver.get(url)
time.sleep(2)

out_dir = r"C:\Users\SK\.gemini\antigravity\brain\c1b884bb-af26-47d8-b057-656fb701cda0"

# Hero Desktop
hero = driver.find_element("id", "home")
driver.execute_script("if (window.lenis) { window.lenis.scrollTo(0, { immediate: true }); } else { window.scrollTo(0, 0); }")
time.sleep(1)
driver.save_screenshot(os.path.join(out_dir, "qa_hero_no_brochure_desktop.png"))
print("Saved qa_hero_no_brochure_desktop.png")

# Footer Desktop
driver.set_window_size(1440, 1200)
footer_bottom = driver.find_element("class name", "avx-footer__bottom")
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'instant', block: 'end' });", footer_bottom)
time.sleep(1)
driver.save_screenshot(os.path.join(out_dir, "qa_footer_no_brochure_desktop.png"))
print("Saved qa_footer_no_brochure_desktop.png")

# Mobile Viewport
driver.set_window_size(390, 844)
driver.execute_script("if (window.lenis) { window.lenis.scrollTo('#home', { immediate: true }); } else { window.scrollTo(0, 0); }")
time.sleep(2)
driver.save_screenshot(os.path.join(out_dir, "qa_hero_no_brochure_mobile.png"))
print("Saved qa_hero_no_brochure_mobile.png")

driver.execute_script("arguments[0].scrollIntoView({ behavior: 'instant', block: 'end' });", footer_bottom)
time.sleep(1)
driver.save_screenshot(os.path.join(out_dir, "qa_footer_no_brochure_mobile.png"))
print("Saved qa_footer_no_brochure_mobile.png")

driver.quit()
print("All screenshots captured successfully!")
