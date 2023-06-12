class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x :x[0])
        i,length = 0, len(intervals) -1
        while i < length:
            if intervals[i][1] >= intervals[i+1][0] and intervals[i][1] <= intervals[i+1][1]:
                intervals[i] = [intervals[i][0],intervals[i+1][1]]
                intervals.pop(i+1)
                length -= 1
            elif intervals[i][1] >= intervals[i+1][1]:
                intervals.pop(i+1)
                length -= 1
            else:
                i += 1
        return intervals
