class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start,end = 0,0
	cursum = 0;
	while True:
	    if cursum < s:

