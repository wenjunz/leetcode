class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        d = {}
        return self._rob(nums,d)
        
    def _rob(self,nums,d,i=0):
        if i in d:
            return d[i]
        if i>=len(nums)-2:
            d[i] = max(nums[i:])
            return d[i]
        d[i] = max(nums[i]+self._rob(nums,d,i+2),self._rob(nums,d,i+1))
        return d[i]
