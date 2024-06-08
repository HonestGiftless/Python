# Добавь разделитель

s = input()
sep = input()

l = []
l.extend(s)
l_s = sep.join(l)

print(l_s)