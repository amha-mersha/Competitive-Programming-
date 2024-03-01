class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(idx,row,col):
            if idx == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col]!= word[idx]:
                return False
            curr = board[row][col]
            board[row][col] = "#"
            found = backtrack(idx+1,row+1,col) or backtrack(idx+1,row,col+1) or backtrack(idx+1,row-1,col) or backtrack(idx+1,row,col-1)
            board[row][col] = curr
            return found
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(0,i,j):
                    return True
        return False