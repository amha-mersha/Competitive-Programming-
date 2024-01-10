class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l,curr = 0,0
        res = len(blocks)
        for r in range(len(blocks)):
            if blocks[r] == "W":
                curr += 1
            while r-l +1 >= k:
                res = min(curr,res)
                if blocks[l] == "W":
                    curr -= 1
                l += 1
        return res