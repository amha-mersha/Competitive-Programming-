class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        res = curr
        for i in range(0,len(nums)-k):
            curr = curr - nums[i] + nums[i+k]
            res = max(curr,res)
        return res/k
