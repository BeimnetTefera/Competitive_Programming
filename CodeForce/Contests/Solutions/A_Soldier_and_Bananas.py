k, n, w = map(int, input().split())
res = 0
for i in range(1, w+1):
    res += (k * i)
if res - n < 0:
    print(0)
else:
    print(res - n)
