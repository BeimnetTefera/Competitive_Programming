n, k = map(int, input().split())

arr_1 = list(map(int, input().split()))

arr_2 = list(map(int, input().split()))

def sort_arr(arr_1, arr_2):
    result = []
    p_1 = 0
    p_2 = 0

    while p_1 < len(arr_1) and p_2 < len(arr_2):
        if arr_1[p_1] <= arr_2[p_2]:
            result.append(arr_1[p_1])
            p_1 += 1
        else:
            result.append(arr_2[p_2])
            p_2 += 1

    result.extend(arr_1[p_1:])
    result.extend(arr_2[p_2:])

    return result

res = sort_arr(arr_1, arr_2)
print(*res)
