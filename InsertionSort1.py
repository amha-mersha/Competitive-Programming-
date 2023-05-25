def insertionSort1(n, arr):
    last = arr[-1]
    i = n - 1
    while i > 0 and arr[i-1] > last :
        arr[i] = arr[i-1]
        print(*arr)
        i -= 1
    arr[i] = last 
    print(*arr)
