class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for i in range(len(matrix)-1):
            if matrix[i][0:-1] != matrix[i+1][1:]:
                return False
        return True
            