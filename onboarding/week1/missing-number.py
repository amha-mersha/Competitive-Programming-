class Solution(object):
    def missingNumber(self, nums):
        nums = set(nums)
        item = 0
        for i in range(len(nums)+1):
            if i not in nums:
                item = i
        return item
        