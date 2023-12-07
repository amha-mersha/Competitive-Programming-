class Solution(object):
    def rearrangeArray(self, nums):
        p,n = 0,1
        res = [0]*len(nums)
        for i in nums:
            if i < 0:
                res[n] = i
                n += 2
            else:
                res[p] = i
                p += 2
        return res