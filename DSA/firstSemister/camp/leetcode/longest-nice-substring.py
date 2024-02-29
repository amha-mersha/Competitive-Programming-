class Solution:
    def longestNiceSubstring(self, s: str) -> str:
            if len(s) < 2:
                return ""
            sSet = set(s)
            for i,itm in enumerate(s):
                if itm.swapcase() not in sSet:
                    leftside = self.longestNiceSubstring(s[:i])
                    rightside = self.longestNiceSubstring(s[i+1:])

                    return leftside if len(leftside) >= len(rightside) else rightside
            return s