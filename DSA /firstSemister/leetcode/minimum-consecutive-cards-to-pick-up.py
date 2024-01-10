class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        curr,res,l = set(),len(cards),0
        for r in range(len(cards)):
            if cards[r] not in curr:
                curr.add(cards[r])
            else:
                while cards[l] != cards[r]:
                    curr.remove(cards[l])
                    l += 1
                res = min(res,r-l+1)
                l += 1
        return res if l != 0 else -1