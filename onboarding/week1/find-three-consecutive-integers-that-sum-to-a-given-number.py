class Solution(object):
    def sumOfThree(self, num):
        mid = num//3
        if mid-1 + mid + mid+1 == num:
            return [mid-1,mid,mid+1]
        return []
        