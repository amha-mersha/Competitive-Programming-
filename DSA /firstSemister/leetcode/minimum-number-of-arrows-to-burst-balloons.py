class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        last_end = points[0][1]
        count = 1
        for start,end in points:
            if start <= last_end:
                continue
            last_end = end
            count += 1
        return count