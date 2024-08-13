# The bracket sequence

def is_correct_bracket(text: str) -> bool:
    result = True
    counter = 0
    
    for i in text:
        if counter >= 0:
            if i == "(":
                counter += 1
            else:
                counter -= 1
        else:
            result = False
            break

    if counter == 0:
        result = True
    else:
        result = False

    return result

txt = input()

print(is_correct_bracket(txt))