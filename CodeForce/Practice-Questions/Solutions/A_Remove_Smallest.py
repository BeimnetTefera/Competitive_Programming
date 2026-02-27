t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    flag = True

    for j in range(n -1):
        if arr[j + 1] - arr[j] > 1:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
