amount = int(input())
marks = [int(input()) for _ in range(amount)]
avr = 0
for i in range(0, len(marks)):
    if marks[i] == 3:
        print("None")
        exit()
    avr += marks[i]
avr = float(avr/len(marks))
if avr == 5:
    print("Named")
elif avr >= 4.5:
    print("High")
else:
    print("Common")