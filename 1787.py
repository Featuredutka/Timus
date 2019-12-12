k, n = [int(x) for x in input().split()]
a = list(map(int, input().split()))
m = 0

for i in a:
    m += i
    if (m - k >= 0):
        m -= k
    else:
        m = 0
print(m)