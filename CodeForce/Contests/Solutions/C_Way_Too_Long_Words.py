n = int(input())
for _ in range(n):
    word = input()
    if len(word) < 10:
        print(word)
    else:
        mid = len(word) - 2
        print(word[0] + str(mid) + word[len(word) - 1])
