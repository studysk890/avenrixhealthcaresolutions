import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

title = re.search(r'<title>(.*?)</title>', html)
print('Title:', title.group(1) if title else 'No title')

meta_desc = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html)
print('Meta Desc:', meta_desc.group(1) if meta_desc else 'No meta description')

sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', html)
print('Sections found:', sections)

nav_links = re.findall(r'href=["\'](#[a-zA-Z0-9_-]+)["\']', html)
print('Anchor links:', list(dict.fromkeys(nav_links)))
