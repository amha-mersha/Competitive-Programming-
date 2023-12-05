class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        total = sum(distance)
        dis = 0
        last = 0
        if start > destination:
            destination += len(distance)
        for i in range(start+1,destination+1):
            dis += distance[(i%len(distance))-1]
        return min(dis,total-dis)

        