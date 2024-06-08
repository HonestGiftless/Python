# Плохие комментарии 😈

for i in range(1, int(input()) + 1):
    comment = input()

    if comment.isspace() or len(comment) == 0:
        print(f"{i}: COMMENT SHOULD BE DELETED")
    else:
        print(f"{i}: {comment}")