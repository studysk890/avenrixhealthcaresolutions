from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1440,1100")

driver = webdriver.Chrome(options=options)
url = "file:///" + os.path.abspath("index.html").replace("\\", "/")
print("Loading:", url)
driver.get(url)
time.sleep(2)

out_dir = r"C:\Users\SK\.gemini\antigravity\brain\c1b884bb-af26-47d8-b057-656fb701cda0"

# Contact Section
contact = driver.find_element("id", "contact")
driver.execute_script("arguments[0].scrollIntoView();", contact)
time.sleep(1)
driver.save_screenshot(os.path.join(out_dir, "qa_contact_updated.png"))
print("Saved qa_contact_updated.png")

# Footer Section
footer = driver.find_element("id", "footer")
driver.execute_script("arguments[0].scrollIntoView();", footer)
time.sleep(1)
driver.save_screenshot(os.path.join(out_dir, "qa_footer_updated.png"))
print("Saved qa_footer_updated.png")

# Mobile Viewport
driver.set_window_size(390, 844)
driver.execute_script("arguments[0].scrollIntoView();", contact)
time.sleep(1)
driver.save_screenshot(os.path.join(out_dir, "qa_contact_mobile.png"))
print("Saved qa_contact_mobile.png")

driver.execute_script("arguments[0].scrollIntoView();", footer)
time.sleep(1)
driver.save_screenshot(os.path.join(out_dir, "qa_footer_mobile.png"))
print("Saved qa_footer_mobile.png")

driver.quit()
print("All screenshots captured successfully!")
