n, k = [int(x) for x in input().split()]
s = list(input().split())
recounter = n//k + 1
iterator = 0
if n % k:
    out = ["" for x in range(n//k+1)]
else:
    out = ["" for x in range(n // k)]
for j in range(0, len(s)):
    if len(s[j]) == 1:
        s[j] = "   " + s[j]
    elif len(s[j]) == 2:
        s[j] = "  " + s[j]
    elif len(s[j]) == 3:
        s[j] = " " + s[j]
    else:
        s[j] = "" + s[j]
for i in range(0, len(s)):
    if iterator == len(out):
        iterator = 0
    out[iterator] = out[iterator] + s[i]
    iterator += 1
for i in range (0, len(out)):
    print(out[i])