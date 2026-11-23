with open('js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function initScrollSpy\(\).*?(?=\nfunction |\Z)', text, re.DOTALL)
if m:
    print(m.group(0))
