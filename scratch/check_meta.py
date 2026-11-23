with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<title>.*?</title>', text)
print(m.group(0) if m else "no title")
m2 = re.search(r'<meta name="description".*?>', text)
print(m2.group(0) if m2 else "no meta desc")
