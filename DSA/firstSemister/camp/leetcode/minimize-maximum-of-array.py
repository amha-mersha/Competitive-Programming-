class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        tot = 0
        mx = 0
        for i,itm in enumerate(nums,start = 1):
            tot += itm
            mx = max(mx,math.ceil(tot/i))
        return mx