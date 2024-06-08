# Автомобильный номер 🚘

def get_correctly(number):
    result = True

    number = number.split('_')

    if len(number[0]) == 6 and 2 <= len(number[1]) <= 3:
        if number[0][0].isalpha() and number[0][4].isalpha() and number[0][5].isalpha() and number[0][0] in "АВЕКМНОРСТУХ" and number[0][4] in "АВЕКМНОРСТУХ" and number[0][5] in "АВЕКМНОРСТУХ":
            if number[0][1].isdigit() and number[0][2].isdigit() and number[0][3].isdigit():
                if len(number[1]) == 2:
                    if number[1][0].isdigit() and number[1][1].isdigit():
                        result = True
                    else:
                        result = False
                else:
                    if number[1][0].isdigit() and number[1][1].isdigit() and number[1][2].isdigit():
                        result = True
                    else:
                        result = False
            else:
                result = False
        else:
            result = False
    else:
        result = False

    return result

number = input()

if get_correctly(number):
    print("YES")
else:
    print("NO")