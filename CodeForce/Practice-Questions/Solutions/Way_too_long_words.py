n = int(input())
for _ in range(n):
    cur_word = input()
    size_word = len(cur_word)
 
    if size_word <= 10:
        print(cur_word)
    else:
        print(cur_word[0] + str((size_word - 2)) + cur_word[-1])
