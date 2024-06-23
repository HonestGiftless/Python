# is_good_password() 👀

def is_good_password(string):
    if len(string) >= 9 and (len([i for i in string if i == i.lower() and i.isalpha()]) > 0 and len([j for j in string if j == j.upper() and j.isalpha()])) > 0 and any(k.isdigit() for k in string):
        return True
    else:
        return False