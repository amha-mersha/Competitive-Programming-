class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        skyline = [[0] * len(grid),[0] * len(grid)]
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid)):
                skyline[0][c] = max(skyline[0][c],grid[r][c])
                skyline[1][r] = max(skyline[1][r],grid[r][c])
        
        for r in range(len(grid)):
            for c in range(len(grid)):
                count += min(skyline[0][c],skyline[1][r])- grid[r][c]
        return count

