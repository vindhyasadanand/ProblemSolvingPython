class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        col = len(matrix[0])
        R = set()
        C = set()
        for i in range(rows):
            for j in range(col):
                if matrix[i][j] ==0:
                    R.add(i)
                    C.add(j)
        for i in range(rows):
            for j in range(col):
                if i in R or j in C:
                    matrix[i][j] = 0
'''
space complexity = O(m+n)
time complexity O(m*n)
'''
