string = input()
digit_string = ''
char_string = ''
other_string = ''
for symbol in string:
    if symbol.isdigit():
        digit_string += symbol
    elif symbol.isalpha():
        char_string += symbol
    else:
        other_string += symbol
print(digit_string)
print(char_string)
print(other_string)