class Solution(object):
    def decompressRLElist(self, nums):
        res = []
        for i in range(len(nums)//2):
            res.extend([nums[i*2+1]]* nums[i*2])
        return res
        