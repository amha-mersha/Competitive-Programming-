class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonal = 0
        col = 0
        for i in range(len(mat)):
            diagonal += mat[i][col]
            col += 1
        col = len(mat)-1
        for i in range(len(mat)):
            diagonal += mat[i][col]
            col -= 1
        if len(mat)%2:
            diagonal -= mat[len(mat)//2][len(mat)//2]
        return diagonal