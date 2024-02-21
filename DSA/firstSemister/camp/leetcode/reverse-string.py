class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(l,r,s):
            if r <= l:
                return s
            s[l],s[r] = s[r], s[l]
            helper(l+ 1 , r - 1,s)
            return s
        return helper(0,len(s)-1,s)
        