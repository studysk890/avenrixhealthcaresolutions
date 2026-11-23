import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def dump_section(name, start_pat, end_pat):
    m = re.search(f'({start_pat}.*?)(?={end_pat})', html, re.DOTALL)
    if m:
        with open(f'scratch/section_{name}.html', 'w', encoding='utf-8') as out:
            out.write(m.group(1))
        print(f"Dumped section_{name}.html ({len(m.group(1))} chars)")

dump_section('home', r'<section[^>]*id=["\']home["\']', r'<section[^>]*id=["\']about["\']')
dump_section('about', r'<section[^>]*id=["\']about["\']', r'<section[^>]*id=["\']solutions["\']')
dump_section('solutions', r'<section[^>]*id=["\']solutions["\']', r'<section[^>]*id=["\']products["\']')
dump_section('products', r'<section[^>]*id=["\']products["\']', r'<section[^>]*id=["\']industries["\']')
dump_section('industries', r'<section[^>]*id=["\']industries["\']', r'<section[^>]*id=["\']why-avenrix["\']')
dump_section('why_avenrix', r'<section[^>]*id=["\']why-avenrix["\']', r'<section[^>]*id=["\']contact["\']')
dump_section('contact', r'<section[^>]*id=["\']contact["\']', r'</main>')
dump_section('header', r'<header', r'<main')
dump_section('footer', r'<footer', r'</body>')
