t = int(input())
word = input()

left = 0
right = 4
diff = []
target = "ACTG"

while right <= t:
    curr = word[left:right]
    val = 0

    for i in range(4):
        direct = abs(ord(curr[i]) - ord(target[i]))
        val += min(direct, 26 - direct)

    diff.append(val)
    left += 1
    right += 1

print(min(diff))
