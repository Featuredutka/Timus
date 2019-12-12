data1 = list(map(int, (input().split(" "))))
data2 = list(map(int, (input().split(" "))))
data3 = list(map(int, (input().split(" "))))

weight1 = data1[0] - data3[0]
weight2 = data1[1] - data2[1]

print(weight1, weight2)
