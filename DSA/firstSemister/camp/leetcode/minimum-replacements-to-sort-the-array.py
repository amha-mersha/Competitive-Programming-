class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        curr = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            front = nums[i]
            if front > curr:
                bucket = math.ceil(front/curr)
                count += bucket - 1
                curr = front//bucket
            else:
                curr = nums[i]
        return count
                
