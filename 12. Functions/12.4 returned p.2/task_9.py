# Змеиный регистр

def convert_to_python_case(text):
    s = ''
    for i in text:
        if i.isupper():
            s += '_'
        s += i.lower()
    return s[1:]

input_text = input()

print(convert_to_python_case(input_text))