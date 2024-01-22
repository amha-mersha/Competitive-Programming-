class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        res = 0
        ones = 0
        for i in s:
            if i == "1":
                ones += 1
        for i in range(len(s)-1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
            res = max(zeros + ones,res)
        return res
