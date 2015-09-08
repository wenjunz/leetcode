class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return 0
        
        i,j = 0,len(nums)-1
        
        while i <= j:
            if nums[j] == val:
                j-=1
            elif nums[i] == val:
                nums[i] = nums[j];
                nums[j] = val;
                i+=1
                j-=1
            else:
                i+=1
        
        return j+1;
