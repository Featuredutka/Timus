import math

kwa = list(input().split())
n = int(kwa[0])
r = float(kwa[1])
xarr = []
yarr = []
for i in range(0, n):
    data = list(input().split())
    xarr.append(float(data[0]))
    yarr.append(float(data[1]))
length = 2 * math.pi * r
if n > 1:
    for k in range(0, n-1):
        length += math.sqrt((xarr[k] - xarr[k+1]) ** 2 + (yarr[k] - yarr[k+1]) ** 2)
    length += math.sqrt((xarr[0] - xarr[n-1]) ** 2 + (yarr[0] - yarr[n-1]) ** 2)

print("%.2f" % length)