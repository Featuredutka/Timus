n = int(input())
matrix = []
for i in range(0, n):
    data = list(input().split())
    matrix.append(data)
res = ""
for i in range(n):
    k = i
    j = 0
    while k >= 0:
        res += (matrix[k][j] + ' ')
        k -= 1
        j += 1
for i in range(1, n):
    k = n - 1
    j = i
    while j != n:
        res += (matrix[k][j] + ' ')
        k -= 1
        j += 1
print(res)