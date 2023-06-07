class Solution(object):
    def kClosest(self, points, k):
        record ={}
        result = []
        for i in range(len(points)):
            record [i]= [points[i][0]**2 + points[i][1]**2]
        record = sorted(record.items(), key=lambda x:x[1])[:k]
        for i in range(k):
            result.append(points[record[i][0]])
        return result
