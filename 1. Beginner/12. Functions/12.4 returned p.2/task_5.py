# Ровно в одном

def is_one_away(word1, word2):
    total = 0

    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                total += 1
    
    if total == len(word1) - 1:
        return True
    else:
        return False

txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))