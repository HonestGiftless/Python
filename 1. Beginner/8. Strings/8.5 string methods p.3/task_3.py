# Проверь никнейм 👩🌶️

nickname = input()

if nickname[0] == "@":
    if 5 <= len(nickname) <= 15:
        if nickname[1:].isalpha():
            if nickname.islower():
                print("Correct")
            else:
                print("Incorrect")
        elif nickname[1:].isdigit():
            print("Correct")
        elif nickname[1:].isalnum():
            if nickname.islower():
                print("Correct")
            else:
                print("Incorrect")
        else:
            print("Incorrect")
    else:
        print("Incorrect") 
else:
    print("Incorrect")