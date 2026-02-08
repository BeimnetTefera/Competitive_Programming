import sys

data = sys.stdin.read().splitlines()
n = int(data[0])

phonebook = {}
for i in range(1, n + 1):
    name, number = data[i].split()
    phonebook[name] = number

for q in data[n + 1:]:
    print(f"{q}={phonebook[q]}" if q in phonebook else "Not found")
