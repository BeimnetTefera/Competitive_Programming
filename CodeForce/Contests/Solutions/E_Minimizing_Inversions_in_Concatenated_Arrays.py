t = int(input())

for i in range(t):
    n = int(input())

    arr = []
    for j in range(n):
        a = list(map(int, input().split()))
        arr.append(a)


    arr.sort(key = lambda x: x[0] + x[1])

    result = []
    for val in arr:
        result.append(val[0])
        result.append(val[1])

    print(" ".join(str(y) for y in result))
