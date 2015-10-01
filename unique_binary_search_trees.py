class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.ntree(n)
        
    def ntree(self,n,d={0:1,1:1,2:2,3:5}):
        if n not in d:
            N = 0
            for i in range(1,n+1):
                N += self.ntree(i-1,d)*self.ntree(n-i,d)
            d[n] = N
        return d[n]
