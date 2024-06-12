# Список data содержит слова на русском языке. Напишите программу, которая сортирует этот список по возрастанию длины слов. В случае, если длины каких-то слов совпадают, – отсортировать эти слова в лексикографическом порядке. Отсортированные слова следует вывести на одной строке, разделив символом пробела.

data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

data.sort()
data.sort(key=lambda x: len(x))

print(*data)