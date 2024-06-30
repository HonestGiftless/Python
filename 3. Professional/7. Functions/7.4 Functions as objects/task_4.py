# remove_marks()

def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    remove_marks.count += 1

    result = ''

    for i in text:
        if i not in marks:
            result += i
    
    return result