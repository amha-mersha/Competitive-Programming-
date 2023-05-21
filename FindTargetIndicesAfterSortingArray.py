class Solution(object):
    def targetIndices(self, nums, target):
        num = []
        nums.sort()
        for j,i in enumerate(nums):
            if i == target:
                num.append(j)
        return num
