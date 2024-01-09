class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a':0,'e':0,'i':0,'o':0,'u':0}
        res = 0
        for i in range(k):
            if s[i] in vowels:
                vowels[s[i]] += 1
                res += 1
        curr = res
        for i in range(0,len(s)-k):
            if s[i] in vowels:
                vowels[s[i]] -= 1
                curr -= 1
            if s[i+k] in vowels:
                vowels[s[i+k]] += 1
                curr += 1
            res = max(res,curr)
        return res
        