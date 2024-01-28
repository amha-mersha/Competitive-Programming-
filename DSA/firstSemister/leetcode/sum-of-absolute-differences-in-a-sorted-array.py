class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1] + nums[i])
        res = [prefix[-1] - (nums[0] * len(nums))]
        for i in range(1,len(nums)):
            res.append((nums[i]*(i+1) - prefix[i]) + prefix[-1] - prefix[i] - (nums[i]*(len(nums) - i-1))) 
        return res