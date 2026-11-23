with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'avenrixhealthcaresolutions@gmail.com' in line:
        start = max(0, i - 10)
        end = min(len(lines), i + 25)
        print(f"=== Occurrence at line {i+1} ===")
        print("".join(lines[start:end]))
