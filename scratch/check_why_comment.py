with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="why-avenrix"')
print(repr(text[pos-250:pos+50]))
