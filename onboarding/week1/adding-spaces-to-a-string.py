class Solution(object):
    def addSpaces(self, s, spaces):
        res = []
        prev = 0
        for i in spaces:
            res.append(s[prev:i])
            prev = i
        res.append(s[prev:])
        return " ".join(res)