n = int(input())
arr = list(map(int, input().split()))

left = 0
right = len(arr) - 1

serja = 0
dima = 0

turn = 1

while left < right:
    if turn == 1: # serja's turn
        if arr[left] > arr[right]:
            serja += arr[left]
            left += 1
        else:
            serja += arr[right]
            right -= 1
        turn -= 1
    if turn == 0:
        if arr[left] > arr[right]:
            dima += arr[left]
            left += 1
        else:
            dima += arr[right]
            right -= 1
        turn += 1

if len(arr) % 2 != 0:
    print(serja + arr[left], dima)
else:
    print(serja, dima)
