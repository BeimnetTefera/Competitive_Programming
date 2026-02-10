<<<<<<< HEAD
n = int(input())
 
for _ in range(n):
    arr = list(map(int, input().split()))
    max_num = max(arr)
    
    if (sum(arr) - max_num) == max_num:
        print("YES")
    else:
        print("NO")
=======
n = int(input())
 
for _ in range(n):
    arr = list(map(int, input().split()))
    max_num = max(arr)
    
    if (sum(arr) - max_num) == max_num:
        print("YES")
    else:
        print("NO")
>>>>>>> 8c937a0ec6fbb98fa2b028d68555399507481414
