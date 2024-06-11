# Анаграммы 1

word1 = input()
word2 = input()

w1 = {}
w2 = {}

for s in word1:
        w1[s] = w1.get(s, 0) + 1
        
for s in word2:
        w2[s] = w2.get(s, 0) + 1
        
if w1 == w2:
        print('YES')
else:
        print('NO')