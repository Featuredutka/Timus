def funck(arr, basearr):
    basearr.append(0)
    equalifier = 1
    for i in range(0, len(basearr)-1):
        if basearr[i] == basearr[i+1]:
            equalifier += 1
        else:
            arr.append(equalifier)
            arr.append(" ")
            arr.append(basearr[i])
            arr.append(" ")
            equalifier = 1
    for j in range(0, len(arr)):
        print(arr[j], end ="")



n = int(input())
basearr = list(map(int, input().split()))
arr = []
funck(arr, basearr)
