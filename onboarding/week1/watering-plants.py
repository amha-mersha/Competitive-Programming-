class Solution(object):
    def wateringPlants(self, plants, capacity):
        steps = 0
        curr = capacity 
        for i in range(len(plants)-1):
            curr -= plants[i]
            steps += 1
            if curr < plants[i+1]:
                steps += (i+1)*2
                curr = capacity
        steps += 1
        return steps