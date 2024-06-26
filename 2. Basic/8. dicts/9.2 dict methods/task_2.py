# Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2: если ключ есть в обоих словарях, добавьте его в результирующий словарь со значением, равным сумме соответствующих значений из первого и второго словаря; если ключ есть только в одном из словарей, добавьте его в результирующий словарь с его текущим значением. Результирующий словарь необходимо присвоить переменной result.

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}

for key, value in dict1.items():
        if key in dict2:
                result[key] = value + dict2[key]
        else:
                result[key] = value

for key, value in dict2.items():
        if key not in result:
                result[key] = value