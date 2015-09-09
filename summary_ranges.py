class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        if len(nums) == 1: return [str(nums[0])]
        
        rlist = [];
        nums.append(nums[-1]+2);
        
        start,prev = nums[0],nums[0];
        i = 1;
        while i < len(nums):
            if prev == nums[i]-1:
                prev = nums[i];
                i+=1;
            else:
                if start == prev: rlist.append(str(start))
                else: rlist.append(str(start)+'->'+str(prev))
                start,prev = nums[i],nums[i];
                i+=1;
        return rlist
        
