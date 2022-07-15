string = input().split()
new_string = ''
for item in string:
    new_string += item * len(item)
print(new_string)
