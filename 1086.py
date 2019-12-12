def isPrime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


a = int(input())
b = []
i = 0
while i < a:
    b.append(int(input()))
    i += 1
i = maximum = 0
for i in range(0, a):
    if b[i] > maximum:
        maximum = b[i]
lst = [0] * maximum
num = 0
i = num
while lst[maximum-1] == 0:
    if isPrime(num):
        lst[i] = num
        i += 1
    num += 1
i = 0
for i in range(0, a):
    b[i] = lst[b[i]-1]
    print(b[i])