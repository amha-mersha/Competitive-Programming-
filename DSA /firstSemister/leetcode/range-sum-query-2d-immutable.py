class NumMatrix(object):

    def __init__(self, matrix):
        self.matrix = matrix
        colum,row = len(matrix[0]),len(matrix)
        self.prefix = [[0]*(colum +1)  for i in range(row + 1)]
        for r in range(1,row + 1):
            sumrow = 0
            for c in range(1,colum +1):
                sumrow += self.matrix[r-1][c-1]
                self.prefix[r][c] = sumrow + self.prefix[r-1][c]

    def sumRegion(self, row1, col1, row2, col2):
        return self.prefix[row2+1][col2+1]-self.prefix[row2+1][col1]-self.prefix[row1][col2+1] + self.prefix[row1][col1]