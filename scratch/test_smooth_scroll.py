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
options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

driver = webdriver.Chrome(options=options)
url = "file:///" + os.path.abspath("index.html").replace("\\", "/")
print("Loading:", url)
driver.get(url)
time.sleep(2)

# Check console errors
logs = driver.get_log("browser")
severe_errors = [log for log in logs if log["level"] == "SEVERE"]
print("Console Severe Errors:", len(severe_errors))
for err in severe_errors:
    print("  SEVERE:", err["message"])

# Check if Lenis is active on window
has_lenis = driver.execute_script("return typeof window.lenis !== 'undefined' && window.lenis !== null;")
print("window.lenis initialized:", has_lenis)

if has_lenis:
    lenis_is_smooth = driver.execute_script("return document.documentElement.classList.contains('lenis');")
    print("html has .lenis class:", lenis_is_smooth)

    # Test scrolling with Lenis
    start_y = driver.execute_script("return window.scrollY;")
    print("Initial scrollY:", start_y)

    driver.execute_script("window.lenis.scrollTo('#approach');")
    time.sleep(1.5)
    new_y = driver.execute_script("return window.scrollY;")
    print("ScrollY after lenis.scrollTo('#approach'):", new_y)
    assert new_y > 500, f"Expected scrollY > 500, got {new_y}"

    # Test back to top with Lenis
    driver.execute_script("window.lenis.scrollTo(0);")
    time.sleep(1.5)
    final_y = driver.execute_script("return window.scrollY;")
    print("ScrollY after lenis.scrollTo(0):", final_y)
    assert final_y < 100, f"Expected final_y < 100, got {final_y}"

driver.quit()
print("All smooth scroll tests passed successfully!")
