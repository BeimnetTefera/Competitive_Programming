def insertionSort1(n, arr):
    # Write your code here
   
    cur = arr[n - 1]
    j = n - 1
    
    while j > 0:
        prev = arr[j - 1]
        if prev > cur:
            arr[j] = prev
            print(*arr)
        else:
            break 
        j -= 1
        
    arr[j] = cur
        
    print(*arr)
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)