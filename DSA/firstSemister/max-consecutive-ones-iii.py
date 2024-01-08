class Solution(object):
    def longestOnes(self, nums, k):
        result = 0
        l = 0
        count = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1
            result = max(result,r-l+1) 
        return result