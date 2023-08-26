class Solution(object):
    def pancakeSort(self, arr):
        i = len(arr)
        result = []
        while i > 0:
            if max(arr[:i]) == arr[i-1]:
                i -= 1
                continue
            elif arr[0] != max(arr[:i]):
                mxIdx= arr.index(max(arr[:i]))
                result.append(mxIdx+1)
                arr = list(reversed(arr[:mxIdx+1])) + arr[mxIdx+1:] 
            arr = list(reversed(arr[:i])) + arr[i:]
            result.append(i)
            i -= 1
                
        
        return result 
# More compact and faster version with the same principle 
class Solution(object):
    def pancakeSort(self, arr):
        n = len(arr)
        res = []
        for i in range(n, 0, -1):
            j = arr.index(i)
            arr[:j+1] = arr[:j+1][::-1]
            arr[:i] = arr[:i][::-1]
            res.append(j+1)
            res.append(i)
        return res 
