class Solution(object):
    def totalNQueens(self, n):
        global count
        count = 0
        negDiag = set()
        posDiag = set()
        colms = set()
        def backtracking(row):
            global count
            if row == n:
                count += 1
                return
            for c in range(n):
                if c in colms or (c+row) in posDiag or (c-row) in negDiag:
                    continue
                negDiag.add(c-row)
                posDiag.add(c+row)
                colms.add(c)
                backtracking(row+1)
                negDiag.remove(c-row)
                posDiag.remove(c+row)
                colms.remove(c)
        backtracking(0)
        return count
