# Хороший пароль

password = input()

is_correct = all([len(password) >= 7, any(map(lambda digit: digit.isdigit(), password)), any(map(lambda lower: lower.islower(), password)), any(map(lambda upper: upper.isupper(), password))])

if is_correct:
    print("YES")
else:
    print("NO")