class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums1 = sorted(nums)
        rlist = [];
        for i in xrange(2**len(nums1)):
            mask = [int(j) for j in list(bin(i)[2:].zfill(len(nums1)))]
            rlist.append([nums1[j] for j in xrange(len(nums1)) if mask[j]==1])
        return rlist
