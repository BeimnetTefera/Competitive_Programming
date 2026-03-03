t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = set(arr)

    ans = "NO"

    for num in s:
        if arr.count(num) % 2 == 1:
            ans = "YES"
            break

    print(ans)
