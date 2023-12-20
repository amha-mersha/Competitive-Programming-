class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row,col = 0,0
        res = []
        for i in range(len(mat)+len(mat[0])-1):
            if i%2 == 0:
                while row in range(0,len(mat)) and col in range(0,len(mat[0])):
                    res.append(mat[row][col])
                    row -= 1
                    col += 1
                row += 1
                col -= 1
                if col + 1 < len(mat[0]):
                    col += 1
                else:
                    row += 1
            else:
                while row in range(0,len(mat)) and col in range(0,len(mat[0])):
                    res.append(mat[row][col])
                    row += 1
                    col -= 1
                row -= 1
                col += 1
                if row + 1 < len(mat):
                    row += 1
                else:
                    col += 1
        return res
                    
