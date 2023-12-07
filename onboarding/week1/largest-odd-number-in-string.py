class Solution(object):
    def largestOddNumber(self, num):
        res = ""
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2:
                res = num[:i+1]
                break
        return res
        