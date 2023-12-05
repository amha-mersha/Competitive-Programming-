class Solution(object):
    def getConcatenation(self, nums):
        ln = len(nums)
        for i in range(ln):
            nums.append(nums[i])
        return nums
        