class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 0
        for num,fr,to in trips:
            n = max(n,to)
        road = [0 for i in range(n+1)]
        for num,fr,to in trips:
            road[fr] += num
            if to != n: 
                road[to] -= num
        if road[0] > capacity:
            return False
        for i in range(1,n+1):
            road[i] += road[i-1]
            if road[i] > capacity:
                return False
        print(road)
        return True
