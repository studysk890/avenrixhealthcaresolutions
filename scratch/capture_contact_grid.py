from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

options = Options()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1440,1200')

driver = webdriver.Chrome(options=options)
driver.get('file:///' + os.path.abspath('index.html').replace('\\', '/'))
time.sleep(2)

# Let's set a tall window size so the entire contact section fits in one screenshot
driver.set_window_size(1440, 1600)
driver.execute_script('''
    const contact = document.getElementById('contact');
    if (window.lenis) {
        window.lenis.scrollTo(contact, {immediate: true});
    } else {
        contact.scrollIntoView();
    }
''')
time.sleep(1)

out_dir = r'C:\Users\SK\.gemini\antigravity\brain\c1b884bb-af26-47d8-b057-656fb701cda0'
driver.save_screenshot(os.path.join(out_dir, 'qa_contact_full_grid.png'))
driver.quit()
print('Full contact grid captured!')
