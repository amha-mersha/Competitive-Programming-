class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()
        count = 0
        l,r = 0,len(nums)-1
        while l < r:
            if nums[l] + nums[r] < target:
                count += r - l
                l += 1
            else:
                r -= 1
        return count

        