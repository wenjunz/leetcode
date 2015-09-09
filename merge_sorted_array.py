class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        n1 = m-1;
        n2 = n-1;

        while n1>=0 and n2>=0:
            if nums1[n1] >= nums2[n2]:
                nums1[n1+n2+1] = nums1[n1];
                n1 -= 1;
            else:
                nums1[n1+n2+1] = nums2[n2];
                n2 -= 1;
        if n1 < 0:
            nums1[:n2+1] = nums2[:n2+1];
