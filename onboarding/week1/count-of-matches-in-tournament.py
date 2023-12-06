class Solution(object):
    def numberOfMatches(self, n):
        res = 0
        while n > 1:
            res += n//2
            n = n//2 + n%2
        return res
        