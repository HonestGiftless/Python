# Исправление дубликатов 🌶️

symbols = input().split()
result = []      

for i in range(len(symbols)):
        if symbols[i] not in result:
                result.append(symbols[i])
        else:
                x = symbols[:i].count(symbols[i])
                result.append(symbols[i]+'_'+str(x))
                
print(*result)