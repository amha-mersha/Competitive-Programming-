class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        l,res,curr = 0,0,0
        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
                curr -= nums[l]
                l += 1
            seen.add(nums[r])
            curr += nums[r]
            res = max(res,curr)
        return res