class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target < matrix[0][0] or target > matrix[-1][-1]: return False
        r = bisect.bisect([row[0] for row in matrix],target)-1;
        i = bisect.bisect_left(matrix[r],target)
        if i!= len(matrix[0]) and matrix[r][i]==target: return True
        else: return False
