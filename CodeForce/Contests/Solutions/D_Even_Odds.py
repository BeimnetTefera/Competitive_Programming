n, k = map(int, input().split())
odds = []
evens = []
for num in range(1, n + 1):
    if num % 2 != 0:
        odds.append(num)
    else:
        evens.append(num)
res = odds + evens
print(odds[k-1])
