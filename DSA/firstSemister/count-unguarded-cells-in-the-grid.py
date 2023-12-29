class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        board = [['' for _ in range(n)] for _ in range(m)]
        for guard in guards:
            row, col = guard
            board[row][col] = 'G'
        for wall in walls:
            row, col = wall
            board[row][col] = 'W'
        
        guarded = len(guards)
        for guard in guards:
            row, col = guard
            i = row-1
            while i >= 0 and board[i][col] != 'W' and board[i][col] != 'G':
                if board[i][col] == '':
                    board[i][col] = 'S'
                    guarded += 1
                i -= 1
            i = row+1
            while i < m and board[i][col] != 'W' and board[i][col] != 'G':
                if board[i][col] == '':
                    board[i][col] = 'S'
                    guarded += 1
                i += 1
            i = col-1
            while i >= 0 and board[row][i] != 'W' and board[row][i] != 'G':
                if board[row][i] == '':
                    board[row][i] = 'S'
                    guarded += 1
                i -= 1
            i = col+1
            while i < n and board[row][i] != 'W' and board[row][i] != 'G':
                if board[row][i] == '':
                    board[row][i] = 'S'
                    guarded += 1
                i += 1
        unguarded = m*n - guarded - len(walls)
        return unguarded