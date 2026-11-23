# -*- coding: utf-8 -*-
"""
Verify that all referenced assets exist on disk and all hash links resolve to valid IDs in index.html.
"""

import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Collect all element IDs
all_ids = set(re.findall(r'id=["\']([^"\']+)["\']', html))
print(f"Total element IDs found in index.html: {len(all_ids)}")

# 2. Check all hash links
hash_links = re.findall(r'href=["\'](#[a-zA-Z0-9_-]+)["\']', html)
unique_hash_links = set(hash_links)

broken_anchors = []
for h in unique_hash_links:
    target_id = h[1:]
    if target_id not in all_ids:
        broken_anchors.append(h)

if broken_anchors:
    print(f"FAILED: Broken internal anchors: {broken_anchors}")
else:
    print(f"PASSED: All {len(unique_hash_links)} internal anchor links point to existing IDs!")

# 3. Check all file assets (src, href)
file_refs = re.findall(r'(?:src|href)=["\']([^"\'#][^"\']*\.(?:css|js|jpg|jpeg|png|svg|pdf|otf|woff2?|ico))["\']', html)
unique_files = set(file_refs)

missing_files = []
for fpath in unique_files:
    # URL decode spaces if needed
    clean_path = fpath.replace('%20', ' ')
    if not os.path.isfile(clean_path):
        missing_files.append(fpath)

if missing_files:
    print(f"FAILED: Missing file references: {missing_files}")
else:
    print(f"PASSED: All {len(unique_files)} local file assets exist on disk!")

# 4. Check for duplicate IDs
id_counts = {}
for m in re.finditer(r'id=["\']([^"\']+)["\']', html):
    _id = m.group(1)
    id_counts[_id] = id_counts.get(_id, 0) + 1

duplicates = {k: v for k, v in id_counts.items() if v > 1}
if duplicates:
    print(f"WARNING: Duplicate IDs found: {duplicates}")
else:
    print("PASSED: Zero duplicate IDs in index.html!")
