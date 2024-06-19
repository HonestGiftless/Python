# print_bar_chart()

from collections import Counter

def print_bar_chart(data, mark):
    count = Counter(data).most_common()

    if type(data) is str:
        for i in count:
            print(f"{i[0]} |{mark * i[1]}")
    else:
        maximal_length = len(max(count, key=lambda item: len(item[0]))[0])
        for i in count:
            if len(i[0]) != maximal_length:
                print(f"{i[0] + " " * (maximal_length - len(i[0]) + 1)}|{mark * i[1]}")
            else:
                print(f"{i[0]} |{mark * i[1]}")