class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse= True)
        res = deque()
        res.append(deck[0])
        for i in range(1,len(deck)):
            res.appendleft(res.pop())
            res.appendleft(deck[i])
        return list(res)