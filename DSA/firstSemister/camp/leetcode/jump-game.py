class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 1
        for i in range(len(nums)):
            mx -= 1
            mx = max(mx,nums[i])
            if mx == 0 and i != len(nums)-1:
                return False
        return True