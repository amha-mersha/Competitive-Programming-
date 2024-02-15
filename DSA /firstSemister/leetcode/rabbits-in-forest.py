class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        track  = {}
        count = 0
        for i in answers:
            if i == 0:
                count += 1
                continue
            if i not in track or i == track[i]:
                count += 1
                count += i
                track[i] = 0
            else:
                track[i] += 1
        return count