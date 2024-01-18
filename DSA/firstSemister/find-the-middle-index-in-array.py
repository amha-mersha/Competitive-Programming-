class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        curr = 0
        for r in range(len(nums)):
            if curr == total-nums[r]-curr:
                return r
            curr += nums[r]
        return -1