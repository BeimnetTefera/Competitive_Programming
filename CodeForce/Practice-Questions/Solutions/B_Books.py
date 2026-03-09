n , time = map(int, input().split())
arr = list(map(int, input().split()))
 
left = 0
cur_time = 0
read = 0
for right in range(n):
    cur_time += arr[right]

    while cur_time > time:
        cur_time -= arr[left]
        left += 1

    read = max(read, right - left + 1)

print(read)
