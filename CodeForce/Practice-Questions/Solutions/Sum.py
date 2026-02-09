n = int(input())
 
for _ in range(n):
    arr = list(map(int, input().split()))
    max_num = max(arr)
    
    if (sum(arr) - max_num) == max_num:
        print("YES")
    else:
        print("NO")