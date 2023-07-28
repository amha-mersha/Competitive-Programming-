#Not efficient first attemp
class Solution(object):
# Not efficient first attemp: recurrsion 
    def missingNumber(self, nums):
        n = 0
        def recurr(n):
            while n < len(nums)+1:
                if n not in nums:
                    return n
                return recurr(n+1)
        return recurr(n)
# Second relatively efficient solution 
    def missingNumber(self, nums):
        total = sum(range(0,len(nums)+1))
        for i in nums:
            total -= i
        return total
    
