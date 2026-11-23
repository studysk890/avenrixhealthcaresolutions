with open('js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'contact', text, re.IGNORECASE)
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 50)
    print(repr(text[start:end]))
