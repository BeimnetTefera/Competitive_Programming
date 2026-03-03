n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
prev = 0
i = 0  
ops_done = 0

while ops_done < k:
    while i < n and a[i] - prev == 0:
        i += 1
    
    if i == n:
        print(0)
    else:
        curr = a[i] - prev
        print(curr)
        prev += curr
    
    ops_done += 1
