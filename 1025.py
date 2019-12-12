amount = int(input())
numbers = sorted([int(i) for i in input().split()])
minimal_amount = amount//2 + 1
reqp = 0
for i in range(0, minimal_amount):
    reqp += numbers[i] // 2 + 1
print(reqp)