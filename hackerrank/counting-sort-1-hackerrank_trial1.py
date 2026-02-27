def countingSort(arr):
    # Write your code here
    result = [0 for i in range(100)]
    for num in arr:
        result[num] += 1
    return result