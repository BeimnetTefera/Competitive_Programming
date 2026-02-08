t = int(input())
for _ in range(t):
    num = int(input())
    if num <= 2:
        print(0)
    else:
        if num % 2 == 0:
            num -= 1
            print(num//2)
        else:
            print(num//2)
