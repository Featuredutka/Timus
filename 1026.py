def quick(data: list) -> list:
    if len(data) <= 1:
        return data
    else:
        point = data[len(data)//2]
        greater = [i for i in data if i > point]
        lesser = [i for i in data if i < point]
        equal = [i for i in data if i == point]
        return quick(lesser) + equal + quick(greater)
n = int(input())
numbers =[]
for i in range(0, n):
    numbers.append(int(input()))
useless = input()
k = int(input())
positions = []
for i in range(0, k):
    positions.append(int(input()))
numbers = quick(numbers)
for i in range(0, k):
    print(numbers[positions[i]-1])