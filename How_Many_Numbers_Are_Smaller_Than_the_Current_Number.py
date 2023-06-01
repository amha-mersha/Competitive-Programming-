class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        temp = sorted(nums)
        counting  = {}
        result = []
        for i in range(len(temp)):
            if temp[i] not in counting :
                counting [temp[i]] = i
        for i in range(len(nums)):
            result.append(counting [nums[i]])
        return result
