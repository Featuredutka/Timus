l, ta, va, vb = [int(x) for x in input().split()]
tb = ta
n = int(input())
for i in range(0, n):
    data = input().split()
    person = int(data[0])
    check = int(data[1])
    check = int(data[2])
    if person - 1:
        tb -= check
    else:
        ta -= check

print(int((va*ta + vb*tb)/l))