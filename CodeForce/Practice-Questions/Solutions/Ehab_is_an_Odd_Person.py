n = int(input())
arr = list(map(int, input().split()))
count_even = count_odd = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        count_even +=1
    if arr[i] % 2 != 0:
        count_odd +=1
if count_even == len(arr) or count_odd == len(arr):
    print (*arr)
else:
    new_arr = sorted(arr)
    print(*new_arr)
