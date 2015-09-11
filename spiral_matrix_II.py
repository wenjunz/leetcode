class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rlist = [[0 for i in xrange(n)] for j in xrange(n)]
        top,bottom = 0,n-1;
        left,right = 0,n-1;
        
        count = 1;
        while count<=n**2:
            for i in range(left,right+1):
                rlist[top][i] = count;
                count+=1;
            top+=1;
            
            for i in range(top,bottom+1):
                rlist[i][right] = count;
                count+=1;
            right-=1;
            
            for i in range(right,left-1,-1):
                rlist[bottom][i] = count;
                count+=1;
            bottom-=1;
            
            for i in range(bottom,top-1,-1):
                rlist[i][left] = count;
                count+=1;
            left+=1;
        return rlist
