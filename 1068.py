number = int(input())
i = abs(number)
summ = 0
while i != 0:
    summ += i
    i = i - 1

if number > 0:
    print(summ)
else:
    print((summ - 1) * -1)
