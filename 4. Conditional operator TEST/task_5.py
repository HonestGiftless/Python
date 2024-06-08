# YES or NO вот в чем вопрос

x = int(input())

if x % 2 != 0:
    print("YES")
elif 2 <= x <= 5:
    print("NO")
elif 6 <= x <= 20:
    print("YES")
else:
    print("NO")