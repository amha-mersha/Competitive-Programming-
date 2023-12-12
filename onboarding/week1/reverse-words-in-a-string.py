class Solution(object):
    def reverseWords(self, s):
        res = []
        s = list(s.split())
        for i in range(len(s)):
            if s:
                res.append(s.pop())
        return " ".join(res).strip()

        