# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.build_tree(nums)
        
    
    def build_tree(self,nums):
        l = len(nums);
        if l==0:
            return None;
        if l==1:
            return TreeNode(nums[0])
        root = TreeNode(nums[l/2])
        root.left = self.build_tree(nums[:l/2])
        root.right = self.build_tree(nums[l/2+1:])
        return root
