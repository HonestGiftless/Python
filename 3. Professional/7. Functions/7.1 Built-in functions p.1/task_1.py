# Lowercase alphabet

def all_alphabet(start, stop):
    if start == stop:
        return chr(start)
    else:
        print(chr(start))
        return all_alphabet(start + 1, stop)

print(all_alphabet(97, 122))