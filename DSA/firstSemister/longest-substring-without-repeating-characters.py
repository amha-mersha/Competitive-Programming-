class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in curr:
                curr.add(s[r])
            else:
                res = max(res,r-l)
                while s[r] in curr:
                    curr.remove(s[l])
                    l += 1
                curr.add(s[r])
        res = max(res,len(s)-l)
        return res 