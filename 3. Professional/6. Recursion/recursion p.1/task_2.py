# Suspiciously simple 🤐

def print_range(i):
    if i <= 100:
        print(i)
        print_range(i + 1)

print_range(1)