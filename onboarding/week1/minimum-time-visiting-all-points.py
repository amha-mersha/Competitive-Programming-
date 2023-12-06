class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        if len(points) == 1:
            return 0
        count = 0
        for i in range(len(points)-1):
            horz = abs(points[i][0] - points[i+1][0])
            vert = abs(points[i][1] - points[i+1][1])
            count += max(horz,vert)
        return count
        