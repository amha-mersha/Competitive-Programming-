class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        l,r = 0,len(nums)-1
        count = 0
        while l < r:
            curr = nums[l] + nums[r]
            if curr > k:
                r -= 1
            elif curr < k:
                l += 1
            else:
                count += 1
                l += 1
                r -= 1
        return count
        