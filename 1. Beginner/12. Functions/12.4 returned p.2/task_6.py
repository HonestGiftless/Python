# Палиндром 🌶️

def is_palindrome(text):
    l = []
    for i in text:
        if i not in ' ,.!?-':
            i = i.upper()
            l.append(i)
    l2 = l[::-1]
    
    total = 0
    for i in range(len(l)):
        if l[i] == l2[i]:
            total += 1
    
    if total == len(l):
        return True
    else:
        return False

txt = input()

print(is_palindrome(txt))