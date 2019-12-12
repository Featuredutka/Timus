b, r, y = map(int, input().split())
n = int(input())
colors = []
bflag = 0
rflag = 0
yflag = 0
for i in range(0, n):
    colors.append(input())
for j in range(0, n):
    if colors[j] == "Blue":
        bflag += 1
    if colors[j] == "Red":
        rflag += 1
    if colors[j] == "Yellow":
        yflag += 1
res = 1
if bflag:
    res = res*b
if rflag:
    res = res*r
if yflag:
    res = res*y
print(res)