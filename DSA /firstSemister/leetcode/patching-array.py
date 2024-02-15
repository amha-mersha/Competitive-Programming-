class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 0
        prefix = 0
        i, length = 0, len(nums)
        while prefix < n:
            if i < length and nums[i] <= prefix + 1:
                prefix += nums[i]
                i += 1
            else:
                prefix += prefix + 1
                patch += 1
        return patch
