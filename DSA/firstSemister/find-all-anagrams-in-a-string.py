class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        pmap = {}
        curr = {}
        res = []

        for i in range(len(p)):
            pmap[p[i]] = pmap.get(p[i], 0) + 1
            curr[s[i]] = curr.get(s[i], 0) + 1

        if curr == pmap:
            res.append(0)

        for i in range(len(p), len(s)):
            curr[s[i]] = curr.get(s[i], 0) + 1
            curr[s[i - len(p)]] -= 1

            if curr[s[i - len(p)]] == 0:
                curr.pop(s[i - len(p)])

            if curr == pmap:
                res.append(i - len(p) + 1)

        return res
