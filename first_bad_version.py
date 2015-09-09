# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start,end = 0,n-1;
        while start < end:
            mid = (start+end)/2;
            if isBadVersion(mid+1):
                end = mid
            else:
                start = mid+1;
        return start+1
