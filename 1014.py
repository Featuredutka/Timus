a = int(input())
b = []
i = 9
if a == 0:
    print(10)
    exit()
elif a == 1:
    print(1)
    exit()
elif a < 10:
    print(a)
    exit()
else:
    while i != 1:
        if a % i == 0:
            a = a / i
            b.append(i)
            i = 9
        else:
            i = i - 1
if a != 1:
    print(-1)
else:
    b = sorted(b)
    r = int("".join(map(str, b)))
    print(r)