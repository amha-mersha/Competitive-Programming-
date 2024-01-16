from collections import defaultdict

class Solution:
    def checker(self,comp: dict, curr: dict) -> bool:
            for i in comp:
                if i not in curr or curr[i] < comp[i]:
                    return False
            return True

    def minWindow(self, s: str, t: str) -> str:
        compare = defaultdict(int)
        for i in t:
            compare[i] += 1

        curr = defaultdict(int)
        res,ind, l = float('inf'),0, 0

        for r in range(len(s)):
            curr[s[r]] += 1
            while self.checker(compare, curr):
                if res > r-l+1:
                    ind = l
                    res = min(r - l + 1, res)
                curr[s[l]] -= 1
                if curr[s[l]] == 0:
                    curr.pop(s[l])
                l += 1

        return "" if res == float('inf') else s[ind:ind+res]
