class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        ans = []
        a, b = 0,0        
        while a < len(firstList) and b < len(secondList):
            if (firstList[a][0] < secondList[b][1] and firstList[a][1] >= secondList[b][0]) or (firstList[a][0] <= secondList[b][1] and firstList[a][1] > secondList[b][0]):
                ans.append([max(firstList[a][0],secondList[b][0]),min(firstList[a][1],secondList[b][1])])
            if firstList[a][1]>= secondList[b][1]:
                b += 1
            else:
                a += 1
        return ans        
