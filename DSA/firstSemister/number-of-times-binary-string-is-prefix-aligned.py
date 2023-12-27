class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        top = 0
        for i in range(len(flips)):
            top = max(top,flips[i])
            if top == i+1:
                count += 1
        return count