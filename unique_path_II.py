class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid);
        n = len(obstacleGrid[0]);
        
        p = [[1 for x in range(n)] for y in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    p[i][j] = (1^obstacleGrid[i][j]);
                elif i==0:
                    p[i][j] = p[i][j-1]*(1^obstacleGrid[i][j])
                elif j==0:
                    p[i][j] = p[i-1][j]*(1^obstacleGrid[i][j])
                else:
                    p[i][j] = (p[i-1][j]+p[i][j-1])*(1^obstacleGrid[i][j])
        
        return p[m-1][n-1]
