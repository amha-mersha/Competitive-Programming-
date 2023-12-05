class Solution(object):
    def printVertically(self, s):
        s = s.split()
        ln = len(max(s,key = len))
        res = [[" "]*len(s) for i in range(ln)]
        for i in range(len(s)):
            for j in range(len(s[i])):
                res[j][i] = s[i][j]
        return [("".join(strr)).rstrip() for strr in res]        

        