useless = input()
first = []
second = []
third = []
first = list(map(int, input().split()))
useless = input()
second = list(map(int, input().split()))
useless = input()
third = list(map(int, input().split()))
cros = list(set(first) & set(second) & set(third))
print(len(cros))