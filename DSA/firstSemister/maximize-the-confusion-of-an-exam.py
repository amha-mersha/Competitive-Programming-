class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        remain,res,l = k,0,0
        for r in range(len(answerKey)):
            if answerKey[r] == "F":
                remain -= 1
            while remain < 0:
                if answerKey[l] == "F":
                    remain += 1
                l += 1
            res = max(res,r-l+1)
        l,remain = 0,k
        for r in range(len(answerKey)):
            if answerKey[r] == "T":
                remain -= 1
            while remain < 0:
                if answerKey[l] == "T":
                    remain += 1
                l += 1
            res = max(res,r-l+1)
        return res

