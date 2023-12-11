class Solution(object):
    def findSpecialInteger(self, arr):
        gap = len(arr)//4
        for i in range(len(arr)-gap):
            if arr[i] == arr[i+gap]:
                return arr[i]
        return -1