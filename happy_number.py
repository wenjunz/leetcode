class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        S = set()
        string = str(n);
        while True:
            tmp = 0;
            for c in string:
                tmp = tmp+int(c)**2;
            if tmp == 1: return True
            elif tmp not in S:
                S.add(tmp);
                string = str(tmp)
            else:
                return False
