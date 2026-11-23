with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's read approach_and_quality from scratch/upgrade_website.py
import re
with open('scratch/upgrade_website.py', 'r', encoding='utf-8') as f:
    up_code = f.read()

m = re.search(r'approach_and_quality = """(.*?)"""', up_code, re.DOTALL)
assert m, "approach_and_quality not found"
approach_and_quality = m.group(1)

target = '<section class="avx-values" id="why-avenrix"'
assert target in html, f"{target} not in html"

html = html.replace(target, approach_and_quality + '\n    ' + target)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Injected approach and quality before why-avenrix successfully!")
