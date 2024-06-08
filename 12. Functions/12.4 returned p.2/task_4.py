# Good password 🌶️

def is_password_good(password):
    ok_pass = 0
    upp = 0
    low = 0
    flag_dig = False

    for i in range(65, 91):
        if str(chr(i)) in password:
            upp += 1

    for i in range(97, 123):
        if str(chr(i)) in password:
            low += 1

    for i in password:
        if i in '0123456789':
            flag_dig = True
            

    if len(password) >= 8:
        ok_pass += 1
    if upp > 0:
        ok_pass += 1
    if low > 0:
        ok_pass += 1
    if flag_dig:
        ok_pass += 1

    if ok_pass == 4:
        return True
    else:
        return False

txt = input()

print(is_password_good(txt))