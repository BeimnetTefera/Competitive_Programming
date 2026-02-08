n = int(input())
word = input()
word = word.upper()

store = {}
for char in word:
    store[char] = store.get(char, 0) + 1

if len(store) != 26:
    print("NO")
else:
    print("YES")   
