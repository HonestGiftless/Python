# Список по образцу 1

# На вход программе подается число 𝑛. Напишите программу, которая создает и выводит построчно список, состоящий из 
# 𝑛 списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

def printLst(lst):
    for i in lst:
        print(i, end='\n')

n = int(input())
elem = [int(i) for i in range(1, n + 1)]
numbers = []

for i in range(n):
    numbers.append(elem)

printLst(numbers)