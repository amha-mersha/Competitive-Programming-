class Solution:
    def addSpaces(self, s, spaces):
        result = []
        lastIndex = 0
        for i in spaces:
            result.append(s[lastIndex:i])
            lastIndex = i
        result.append(s[lastIndex:])
        return " ".join(result)
