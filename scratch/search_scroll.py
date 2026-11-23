import glob
import re

for ext in ['css/*.css', 'js/*.js']:
    for fpath in glob.glob(ext):
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        matches = [m.strip() for m in re.findall(r'[^\n]*scroll[^\n]*', content, re.IGNORECASE)]
        if matches:
            print(f"=== {fpath} ({len(matches)} occurrences) ===")
            for m in matches[:10]:
                print("  ", m[:100])
