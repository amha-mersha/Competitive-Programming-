class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for i in range(len(tickets)):
            if i < k:
                count += min(tickets[k],tickets[i])
            elif i == k:
                count += tickets[k]
            else:
                count += min(tickets[k]-1,tickets[i])
        return count