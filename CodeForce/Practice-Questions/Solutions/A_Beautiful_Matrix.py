matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

rows = len(matrix)
cols = len(matrix[0])
count = 0 
for row in range(rows):
    for col in range (cols):
        if matrix[row][col] == 1:
            count = abs(2 - row) + abs(2 - col)
print(count)