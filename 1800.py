data = input()
mdata = data.split()
l = int(mdata[0]) / 100
h = int(mdata[1]) / 100
w = int(mdata[2]) / 60
if l/2 < h:
t = (2 * (h - l / 2) / 9.81) ** 0.5
a = w * t
if 0.25 < a % 1 < 0.75:
print("bread")
else:
print("butter")
else:
print("butter")
