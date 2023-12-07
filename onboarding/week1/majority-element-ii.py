class Solution(object):
    def majorityElement(self, nums):
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        three = len(nums)/3
        res = []
        for i in d:
            if d[i] > three:
                res.append(i)
        return res
        