class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_h,water = [0]*len(height),[0]*len(height)
        max_left, max_right = 0,0
        for i in xrange(len(height)):
            max_left = max(max_left,height[i])
            left_h[i] = max_left;
        
        for i in xrange(len(height)-1,-1,-1):
            max_right = max(max_right,height[i]);
            water[i] = min(left_h[i],max_right);
        
        return sum(water)-sum(height)
