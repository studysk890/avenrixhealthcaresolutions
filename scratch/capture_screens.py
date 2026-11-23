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
driver.save_screenshot(os.path.join(out_dir, "qa_upgrade_desktop_hero.png"))
print("Saved qa_upgrade_desktop_hero.png")

# Scroll down to approach and quality
approach = driver.find_element("id", "approach")
driver.execute_script("arguments[0].scrollIntoView();", approach)
time.sleep(1)
driver.save_screenshot(os.path.join(out_dir, "qa_upgrade_approach.png"))
print("Saved qa_upgrade_approach.png")

# Scroll down to partnerships and faqs
partnerships = driver.find_element("id", "partnerships")
driver.execute_script("arguments[0].scrollIntoView();", partnerships)
time.sleep(1)
driver.save_screenshot(os.path.join(out_dir, "qa_upgrade_partnerships.png"))
print("Saved qa_upgrade_partnerships.png")

# Scroll down to contact
contact = driver.find_element("id", "contact")
driver.execute_script("arguments[0].scrollIntoView();", contact)
time.sleep(1)
driver.save_screenshot(os.path.join(out_dir, "qa_upgrade_contact.png"))
print("Saved qa_upgrade_contact.png")

# Mobile viewport
driver.set_window_size(390, 844)
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)
driver.save_screenshot(os.path.join(out_dir, "qa_upgrade_mobile_hero.png"))
print("Saved qa_upgrade_mobile_hero.png")

driver.quit()
print("Done!")
