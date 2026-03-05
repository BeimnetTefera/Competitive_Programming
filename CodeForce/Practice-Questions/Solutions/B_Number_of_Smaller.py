n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def lesser_values(arr1, arr2):
    p1 = 0
    p2 = 0
    cnt = 0

    result = []
    while p1 < n and p2 < m:

        if arr1[p1] < arr2[p2]:
            cnt += 1
            p1 += 1
        else:
            result.append(cnt)
            p2 += 1

    
    while len(result) < m:
        result.append(n)
        
    return result

res = lesser_values(arr1, arr2)
print(*res)
