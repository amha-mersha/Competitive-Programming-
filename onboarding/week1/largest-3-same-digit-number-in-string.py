class Solution(object):
    def largestGoodInteger(self, num):
        res = ""
        for i in range(len(num)-2):
            sub = num[i:i+3]
            if sub[0] == sub[1] == sub[2]:
                res = max(sub,res)
        return res
        