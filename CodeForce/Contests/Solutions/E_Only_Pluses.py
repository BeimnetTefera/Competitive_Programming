t = int(input())
for _ in range(t):
    a, b, c = sorted(map(int, input().split()))
    
    for _ in range(5):
        if a <= b and a <= c:
            a += 1
        elif b <= a and b <= c:
            b += 1
        else:
            c += 1
    
    print(a * b * c)
