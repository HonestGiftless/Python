# Анаграммы 2

def stripSymbols(flist, nlist):
    for i in flist:
        i = i.strip('.,!?:;-')
        nlist.append(i)

sent1 = input().lower().split()
sent2 = input().lower().split()

snt1 = []
snt2 = []

stripSymbols(sent1, snt1)
stripSymbols(sent2, snt2)

rs1 = {}
rs2 = {}

for i in snt1:
    for j in i:
        rs1[j] = rs1.get(j, 0) + 1
        
for i in snt2:
    for j in i:
        rs2[j] = rs2.get(j, 0) + 1

if rs1 == rs2:
    print('YES')
else:
    print('NO')