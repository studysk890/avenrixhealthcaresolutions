with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

def show_section_snippet(sec_id):
    pattern = rf'(<section[^>]*id=["\']{sec_id}["\'].*?)(?=<section|<footer>|$)'
    m = re.search(pattern, html, re.DOTALL)
    if m:
        snippet = m.group(1)[:500]
        print(f"=== SECTION #{sec_id} (Length: {len(m.group(1))}) ===")
        print(snippet)
        print("...\n")
    else:
        print(f"Section #{sec_id} NOT found!")

for s in ['home', 'about', 'solutions', 'products', 'industries', 'why-avenrix', 'contact']:
    show_section_snippet(s)
