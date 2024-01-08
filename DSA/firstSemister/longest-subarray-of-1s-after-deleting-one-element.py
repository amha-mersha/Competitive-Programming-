class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = z = m = 0
        for r in range(len(nums)):
            k = nums[r]
            if k == 0:
                z += 1

            while z > 1:
                if nums[l] == 0:
                    z -= 1
                l += 1
            m = max(m, r - l) 

        return len(nums) - 1 if z == 0 else  m
            