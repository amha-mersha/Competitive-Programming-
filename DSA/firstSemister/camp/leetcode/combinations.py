class Solution:
    def __init__(self):
        self.all = []
    def combine(self, n: int, k: int, start = 1, curr = []) -> List[List[int]]:
        if k == 0:
            self.all.append(curr.copy())
            return 
        for i in range(start,n+1):
            curr.append(i)
            self.combine(n,k-1,i+1,curr)
            curr.pop()
        return self.all