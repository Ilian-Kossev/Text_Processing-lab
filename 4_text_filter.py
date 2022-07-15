banned_words = input().split(', ')
text = input()
for item in banned_words:
    while item in text:
        new_item = len(item)*'*'
        text = text.replace(item, new_item)
print(text)