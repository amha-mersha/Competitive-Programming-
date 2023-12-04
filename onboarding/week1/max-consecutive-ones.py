class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        curr = 0
        res = 0
        for i in nums:
            if i :
                curr += 1
            else:
                curr = 0
            res = max(res,curr)
        return res
        