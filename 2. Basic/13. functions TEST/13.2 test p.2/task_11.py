# Сортировка IP-адресов

def get_size(ip):
    new_ip = ip.split(".")

    total = 0
    start_size = 3

    for i in new_ip:
        total += int(i) * 256**start_size
        start_size -= 1
    
    return ip, total

ips = [input() for _ in range(int(input()))]
sizes = {k: v for k, v in list(map(get_size, ips))}
sizes = dict(sorted(sizes.items(), key=lambda item: item[1]))

for k in sizes:
    print(k)