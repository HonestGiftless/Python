# Переворот числа

def switch(txt):
    if (len(txt) == 5):
        checkFirstZero(txt[::-1])
    else:
        first_symb = txt[0]
        txt = txt[1:]
        txt = first_symb + txt[::-1]
        checkFirstZero(txt)
        
def checkFirstZero(txt):
    while (txt[0] == '0'):
        txt = txt[1:]
        
    print(txt)
    
text = input()

switch(text)