class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []: return 0
        elif target > nums[-1]: return len(nums);
        elif target < nums[0]: return 0;
        
        a = 0;
        b = len(nums)-1;
        
        while a<b-1:
            mid = (b-a)/2 + a
            if target == nums[mid]: 
                return mid;
            elif target > nums[mid]:
                a = mid;
            else:
                b = mid;
        if target == nums[a]: return a
        elif target == nums[b]: return b
        else: return a+1
