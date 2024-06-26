# Forbidden words 🌶️

with open(input(), "r", encoding="utf-8") as file, open("forbidden_words.txt", "r", encoding="utf-8") as forbidden_file:
    forbidden_words = forbidden_file.read().split()

    for s in file:
        for x in forbidden_words:
            while x in s.lower():
                index = s.lower().index(x)
                s = s[:index] + '*' * len(x) + s[index + len(x):]
        print(s.strip())