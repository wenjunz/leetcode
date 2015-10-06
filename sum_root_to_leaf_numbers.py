# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        p = self.path(root)
        return sum(map(int,p))
        
    def path(self,root):
        if not root:
            return ''
        if not root.left and not root.right:
            return [str(root.val)]
        else:
            tail_left = [v for v in self.path(root.left)]
            tail_right = [v for v in self.path(root.right)]
        return [str(root.val) + u for u in tail_left + tail_right]

