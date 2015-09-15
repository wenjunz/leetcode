class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        rlist = [1]*len(nums);
        prod1 = 1;
        for i in xrange(1,len(nums)):
            prod1 *= nums[i-1]
            rlist[i] = prod1;
        
        prod2 = 1;
        for i in xrange(len(nums)-2,-1,-1):
            prod2 *= nums[i+1]
            rlist[i] = rlist[i]*prod2;
        return rlist
