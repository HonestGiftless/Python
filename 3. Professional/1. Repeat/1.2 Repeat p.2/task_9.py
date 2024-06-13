# Файлы в файле 🌶️🌶️

dct = dict()
dct_size = dict()
result = list()

with open('files.txt', 'r', encoding='utf-8') as file:
    for i in file:
        i = i.strip('\n').split()
        
        if i[-1] == 'KB':
            dct_size[i[0]] = int(i[1]) * 1024
        elif i[-1] == 'MB':
            dct_size[i[0]] = int(i[1]) * 1024 * 1024
        elif i[-1] == "GB":
            dct_size[i[0]] = int(i[1]) * 1024 * 1024 * 1024
        elif i[-1] == "B":
            dct_size[i[0]] = int(i[1])


    for k, v in dct_size.items():
        format = k.split('.')[1]
        if format not in dct.keys():
            dct[format] = [[k, v]]
        else:
            dct[format] += [[k, v]]

    dct = dict(sorted(dct.items()))

    fk = ''

    for k in dct.keys():
        fk = k
        break
    
    for k, v in dct.items():
        lst = [i[0] for i in v]
        lst = list(sorted(lst))
        total = sum([i[1] for i in v])

        if k != fk:
            print("\n", *lst, sep='\n')
        else:
            print(*lst, sep='\n')
        print("----------")
        
        if int(round(total / 1024 / 1024 / 1024)) >= 1:
            print("Summary:", int(round(total / 1024 / 1024 / 1024)), "GB", end='')
        elif int(round(total / 1024 / 1024)) >= 1:
            print("Summary:", int(round(total / 1024 / 1024)), "MB", end='')
        elif int(round(total / 1024)) >= 1:
            print("Summary:", int(round(total / 1024)), "KB", end='')
        else:
            print("Summary:", int(round(total)), "B", end='')