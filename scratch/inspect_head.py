with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
head_match = re.search(r'<head>(.*?)</head>', html, re.DOTALL)
if head_match:
    head = head_match.group(1)
    for m in re.finditer(r'<link[^>]*rel=["\']stylesheet["\'][^>]*>', head):
        print(m.group(0))
