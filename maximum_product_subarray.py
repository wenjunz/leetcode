class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending_here = min_ending_here = max_so_far = min_so_far = nums[0]

        for i in nums[1:]:
            max_ending_here,min_ending_here = \
                max([i,i*max_ending_here,i*min_ending_here]),min([i,i*max_ending_here,i*min_ending_here])
            max_so_far = max(max_so_far,max_ending_here)
            min_so_far = min(min_so_far,min_ending_here)
        return max_so_far
