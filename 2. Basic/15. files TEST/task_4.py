# Самое длинное слово в файле

with open('words.txt', 'r', encoding='utf-8') as file:
    words_list = file.readline().split()
    result = list()

    max_word = max(words_list, key=len)
    length_max_word = len(max_word)
    
    for i in words_list:
        if len(i) == length_max_word:
            result.append(i)
    
    print(*result, sep='\n')