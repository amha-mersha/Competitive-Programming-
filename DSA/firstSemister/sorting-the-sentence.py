class Solution:
    def sortSentence(self, s: str) -> str:
        s = s[::-1]
        s = list(s.split())
        s.sort(key = lambda x: x[0])
        for i in range(len(s)):
            s[i] = s[i][1:]
            s[i] = s[i][::-1]
        return " ".join(s)