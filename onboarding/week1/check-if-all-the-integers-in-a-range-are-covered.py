class Solution(object):
    def isCovered(self, ranges, left, right):
        wide = set()
        for i,j in ranges:
            wide.update(range(i,j+1))
        for i in range(left,right+1):
            if i not in wide:
                return False
        return True 
        