class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        T_i = triangle[0];
        
        for i in range(1,len(triangle)):
            tmp = [0]*(len(T_i)+1)
            tmp[0] = T_i[0] + triangle[i][0]
            for n in range(1,len(T_i)):
                tmp[n] = min(T_i[n-1],T_i[n])+triangle[i][n]
            tmp[-1] = T_i[-1] + triangle[i][-1]
            T_i = tmp;
            print T_i
        return min(T_i)
