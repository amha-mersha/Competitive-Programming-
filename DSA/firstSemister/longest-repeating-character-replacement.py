class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        letter = collections.defaultdict(int)
        res = 0
        maxf = 0
        for r,item in enumerate(s):
            letter[item] += 1
            maxf = max(maxf,letter[item])
            while (r-l+1) - maxf > k:
                letter[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res