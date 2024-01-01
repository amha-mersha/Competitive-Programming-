
class Solution(object):
    def maxCoins(self, piles):
        piles = sorted(piles,reverse=True)
        count = 0
        for i in range(1,2*len(piles)//3,2):
            count += piles[i]
        return count