amount = int(input())
guests = [input() for _ in range(amount)]
sub = "+"
add = len(guests)+2
for string in guests:
    if sub in string:
        add += 1
if add == 13:
    add += 1
print(add*100)