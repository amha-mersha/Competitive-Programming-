class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = self.getRow(rowIndex-1)
        new = []
        for i in range(1,len(res)):
            new.append(res[i-1]+res[i])
        return [1] + new + [1]