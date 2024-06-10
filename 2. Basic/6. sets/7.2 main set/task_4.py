# Дополните приведенный код, чтобы он вывел элементы множества fruits, каждый на отдельной строке, отсортированные по убыванию (в обратном лексикографическом порядке).

fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
fruits = sorted(fruits, reverse=True)

print(*fruits, sep='\n')