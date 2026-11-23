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
driver.get(url)
time.sleep(2)

out_dir = r"C:\Users\SK\.gemini\antigravity\brain\c1b884bb-af26-47d8-b057-656fb701cda0"

# Quality Assurance
quality = driver.find_element("id", "quality")
driver.execute_script("arguments[0].scrollIntoView();", quality)
time.sleep(1)
driver.save_screenshot(os.path.join(out_dir, "qa_upgrade_quality.png"))

# FAQs
faqs = driver.find_element("id", "faqs")
driver.execute_script("arguments[0].scrollIntoView();", faqs)
time.sleep(1)
driver.save_screenshot(os.path.join(out_dir, "qa_upgrade_faqs.png"))

# Also click on FAQ item 2 to test accordion interaction
faq2_trigger = driver.find_elements("class name", "avx-faq-trigger")[1]
driver.execute_script("arguments[0].click();", faq2_trigger)
time.sleep(0.5)
driver.save_screenshot(os.path.join(out_dir, "qa_upgrade_faqs_interactive.png"))

driver.quit()
print("Saved quality and faqs screenshots!")
