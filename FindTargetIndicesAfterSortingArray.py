class Solution(object):
    def targetIndices(self, nums, target):
        num = []
        nums.sort()
        for j,i in enumerate(nums):
            if i == target:
                num.append(j)
        return num
#another solution 
class Solution(object):
    def targetIndices(self, nums, target):
        count = 0
        dups = 0
        for i in nums:
            if i == target:
                dups += 1  
            elif i < target:
                count += 1
        return list(range(count,count+dups))
