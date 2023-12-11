class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        evens = sum(x for x in nums if not x%2)
        ans = []
        for val,i in queries:
            if not nums[i] % 2:
                evens -= nums[i]
            nums[i] += val
            if not nums[i] % 2:
                evens += nums[i]
            ans.append(evens)
        return ans 
            
        