# Панграммы

def is_pangram(text):
    s = set(text.lower())
    if len(s) == 27:
        return True
    else:
        return False


text = input()

print(is_pangram(text))