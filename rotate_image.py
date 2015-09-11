class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix);
        for i in xrange(n):
            for j in xrange(i+1,n):
                a = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = a
        for i in xrange(n):
            matrix[i].reverse()
