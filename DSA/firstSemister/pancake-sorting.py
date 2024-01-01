class Solution(object):
    def pancakeSort(self, arr):
        n = len(arr)
        result = []
        for i in range(n,0,-1):
            j = arr.index(i)
            if arr[n-1] == i:
                n -= 1
                continue
            elif arr[0] != i:
                arr[:j+1] = arr[:j+1][::-1]
                result.append(j+1)
            arr[:n] = arr[:n][::-1]
            result.append(n)
            n -= 1
        return result   