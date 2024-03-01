class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [['.'] * n for i in range(n)]
        posdiag = set()
        negdiag = set()
        columns = set()
        def backtrack(row):
            nonlocal result, board, posdiag, negdiag
            if row == n:
                result.append(["".join(board[i]) for i in range(n)])
                return 
            for i in range(n):
                if i in columns or row-i in posdiag or row + i in negdiag:
                    continue
                board[row][i] = "Q"
                posdiag.add(row-i)
                negdiag.add(row + i)
                columns.add(i)
                backtrack(row+1) 
                posdiag.remove(row-i)
                negdiag.remove(row+i)
                columns.remove(i)
                board[row][i] = "."
            return 
        backtrack(0)
        return result
