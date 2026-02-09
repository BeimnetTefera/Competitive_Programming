t = int(input())
for _ in range(t):
    num = int(input())
    if num <= 3:
        print(num)
    elif num % 2 == 0:
        print(0)
    else:
        print(1)
