class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return [];
        m,n = len(matrix),len(matrix[0])
        if m == 1: return [matrix[0][i] for i in xrange(n)];
        if n == 1: return [matrix[i][0] for i in xrange(m)]
        
        top,bottom = 0,m-1;
        left,right = 0,n-1;
        
        rlist = [];
        while 1:
            rlist.extend([matrix[top][i] for i in xrange(left,right+1)])
            top += 1;
            if len(rlist) >= m*n: break
            rlist.extend([matrix[i][right] for i in xrange(top,bottom+1)])
            right -= 1;
            if len(rlist) >= m*n: break
            rlist.extend([matrix[bottom][i] for i in xrange(right,left-1,-1)])
            bottom -= 1;
            if len(rlist) >= m*n: break
            rlist.extend([matrix[i][left] for i in xrange(bottom,top-1,-1)])
            left += 1;
            if len(rlist) >= m*n: break
        return rlist
