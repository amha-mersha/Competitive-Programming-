def CountSort( arr):
    count = [0 for i in range(max(arr)+1)]
    output = [0 for i in range(len(arr))]
    for i in arr:
        count[i] += 1
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for i in arr:
        output[count[i]-1] = i
        count[i] -= 1
    return output
