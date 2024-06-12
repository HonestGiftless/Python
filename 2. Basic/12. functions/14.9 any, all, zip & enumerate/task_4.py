# Корректный IP-адрес

def is_ip(lst):
    result = list()
    for i in lst:
        if i.isdigit() and 0 <= int(i) <= 255:
            result.append(True)
        else:
            result.append(False)

    return result

ip = input().split('.')
res = is_ip(ip)

print(all(res))