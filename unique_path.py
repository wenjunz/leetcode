class Solution(object):
    def _path(self,m,n,d):
        if m==1 or n==1:
            return 1;
        elif (m,n) in d.keys():
            return d[(m,n)]
        else:
            d[(m,n)] = self._path(m-1,n,d) + self._path(m,n-1,d)
            return d[(m,n)]
            
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = dict();
        return self._path(m,n,d)
