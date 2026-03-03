t = int(input())

for i in range(t):
    size = int(input()) - 2
    arr = list(map(int, input().split()))

    arr.sort()
    min_diff = float('inf')

    for j in range(size):
        diff = (arr[j + 2] - arr[j + 1])  + (arr[j + 1]  - arr[j])

        if diff < min_diff:
            min_diff = diff
            
    print(min_diff)
