class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mini = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] != "." and board[row][col] in mini[(row//3,col//3)]:
                    return False
                elif board[row][col] != ".":
                    mini[(row//3,col//3)].add(board[row][col])
                    
                if board[row][col] != "." and board[row][col] in rows[row]:
                    return False
                elif board[row][col] != ".":
                    rows[row].add(board[row][col])
                    
                if board[row][col] != "." and board[row][col] in cols[col]:
                    return False
                elif board[row][col] != ".":
                    cols[col].add(board[row][col])
        return True