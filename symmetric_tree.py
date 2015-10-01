# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self._symm(root.left,root.right);
        
    def _symm(self,left,right):
        if left and right:
            return left.val==right.val and self._symm(left.left,right.right) and self._symm(left.right,right.left)
        elif not left and not right:
            return True
        else:
            return False
