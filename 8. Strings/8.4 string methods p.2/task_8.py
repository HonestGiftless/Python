# Удаление фрагмента

s = input()

fs = s.find('h')
ss = s.rfind('h')

print(s[0:fs], s[ss + 1:], sep='')