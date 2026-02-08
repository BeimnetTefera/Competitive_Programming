from math import ceil, floor
t = int(input())
for _ in range(t):
    num = int(input())
    if num <= 2:
        print(2)
    else:
        rem = num % 3
        val = num // 3
        result = (floor(val) * 3) - (ceil(val) * 3) + rem
        print(result)
