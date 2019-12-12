def fuckfun(n, m, s, amount):
    while len(s):
        newstring = s[:m]
        flag = False
        for j in range(0, len(newstring)):
            if flag:
                break
            elif not (newstring[j].islower() or newstring[j].isalpha() or newstring[j] == ' '):
                if j + 1 > n:
                    s = s[j:]
                else:
                    s = s[n:]
                amount += 1
                flag = True
                break
            elif flag is False and j == len(newstring) - 1:
                amount += 1
                s = s[m:]
                break
    print(amount)

n, m = map(int, input().split())
s = input()
fuckfun(n, m, s, 0)
