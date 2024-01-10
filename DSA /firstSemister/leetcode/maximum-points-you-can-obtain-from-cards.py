class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr = sum(cardPoints[:len(cardPoints)-k])
        tot = sum(cardPoints)
        res = curr
        gap = len(cardPoints)-k
        for r in range(k):
            curr -= cardPoints[r]
            curr += cardPoints[r+gap]
            res = min(res,curr)
        return tot - res
