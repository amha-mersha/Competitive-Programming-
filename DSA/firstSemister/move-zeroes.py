class Solution(object):
    def moveZeroes(self, nums):
        if len(nums)  == 0:
            return
        if 0 in nums:
            i = nums.index(0)
            j = i + 1
            while j < len(nums):
                if nums[j] != 0:
                    nums[i],nums[j] = nums[j],nums[i]
                    i += 1
                j += 1