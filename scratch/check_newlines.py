with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('<title>')
print(repr(text[pos:pos+300]))
