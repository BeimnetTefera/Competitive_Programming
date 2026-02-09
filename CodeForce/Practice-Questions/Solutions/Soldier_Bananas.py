def Soldier_banana (k, n, w):
    total_cost = 0
 
    for i in range(1, w + 1):
        total_cost += (i * k)
 
    if total_cost <= n:
        return 0
    else:
        return (total_cost - n)
 
k, n, w = map(int, input().split())
print(Soldier_banana (k, n, w))