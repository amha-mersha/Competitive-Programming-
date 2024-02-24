class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        inc = [-1]*len(arr)
        dec = [-1]*len(arr)
        stack = []
        arr.append(0)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                inc[stack[-1]] = i
                stack.pop()
            stack.append(i)
        stack = []
        arr.pop()
        arr.insert(0,0)
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] > arr[i]:
                dec[stack[-1]-1] = i-1
                stack.pop()
            stack.append(i)
        res = 0
        arr.pop(0)
        for i in range(len(arr)):
            res += (inc[i]-i)*(i-dec[i])*arr[i]
        return res%(10**9+7)
        
