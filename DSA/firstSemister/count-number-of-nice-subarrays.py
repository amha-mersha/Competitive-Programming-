class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l,count,res = 0,0,0
        for r in range(len(nums)):
            if nums[r] & 1:
                k -= 1
                count = 0
            while k == 0:
                k += nums[l] & 1
                l += 1
                count += 1
            res += count
        return res