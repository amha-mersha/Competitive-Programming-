class Solution(object):
    def minOperations(self, boxes):
        res = [0]*len(boxes)
        lcst,lcnt,rcst,rcnt = 0,0,0,0
        for i in range(1,len(boxes)):
            lcnt += int(boxes[i-1])
            lcst += lcnt
            res[i] = lcst
        for i in range(len(boxes)-2,-1,-1):
            rcnt += int(boxes[i+1])
            rcst += rcnt
            res[i] += rcst
        return res