class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:x[0]-x[1])
        cost = 0
        i = 0
        while i < len(costs)//2:
            cost += costs[i][0]
            i += 1
        while i < len(costs):
            cost += costs[i][1]
            i += 1
        return cost