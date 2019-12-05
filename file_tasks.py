
with open('referat.txt', 'r', encoding='utf-8') as referat:
    content = referat.read()
print(len(content))
letters = content.split()
print(len(letters))
content = content.replace('.', '!')

with open('referat2.txt', 'w', encoding='utf-8') as referat2:
    referat2.write(content)

