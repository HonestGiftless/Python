# CSV-файл

def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        dict_list = list()
        test = list()
        file.seek(0)

        for i in range(len(lst)):
            test.append(file.readline().strip('\n').split(','))

        for i in range(1, len(test)):
            dct = dict()
            for j in range(len(test[i])):
                dct[test[0][j]] = test[i][j]
            dict_list.append(dct)

        return dict_list