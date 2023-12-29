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