class Solution(object):
    def numIdenticalPairs(self, nums):
        count = defaultdict(int)
        res = 0
        for i in nums:
            res += count[i]
            count[i] += 1
        return res

        #3