def get_phone(text):
    needed_num = (i for i in text.split() if '-' in i)
    result = list()

    for i in needed_num:
        phone = [j.strip('+-.!*?:,') for j in i.split('-')]

        if len(phone[0]) == 1:
            if phone[0].find('7') == 0 or phone[0].find('8') == 0:
                if all(True if j.isdigit() else False for j in phone):
                    if len(phone) == 5:
                        if len(phone[1]) == 3 and len(phone[2]) == 3 and len(phone[3]) == 2 and len(phone[4]) == 2:
                            test = "-".join(phone)
                            if '7' + test[1:] not in result and '8' + test[1:] not in result:
                                result.append(test)
                    elif len(phone) == 4:
                        if len(phone[1]) == 3 and len(phone[2]) == 4 and len(phone[3]) == 4:
                            test = "-".join(phone)
                            if '7' + test[1:] not in result and '8' + test[1:] not in result:
                                result.append(test)
        
    print(*result, sep='\n')

get_phone(input())