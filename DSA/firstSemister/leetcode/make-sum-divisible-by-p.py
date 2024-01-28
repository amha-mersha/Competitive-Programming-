from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        res = float('inf')
        tot = sum(nums)
        
        if tot % p == 0:
            return 0
        
        target_remainder = tot % p
        remainder_index = {0: -1}
        curr_sum = 0
        
        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % p
            complement = (curr_sum - target_remainder) % p
            if complement in remainder_index:
                res = min(res, i - remainder_index[complement])
            remainder_index[curr_sum] = i

        return res if res != float('inf') and res != len(nums) else -1


