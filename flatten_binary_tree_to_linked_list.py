# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.flat(root)
        
    def flat(self,root):
        if not root:
            return None
        if root.left and root.right:
            r_leaf = self.flat(root.right)
            l_leaf = self.flat(root.left)
            l_leaf.right = root.right;
            root.right = root.left
            root.left = None
            return r_leaf
        elif root.right:
            r_leaf = self.flat(root.right)
            return r_leaf
        elif root.left:
            l_leaf = self.flat(root.left)
            root.right = root.left
            root.left = None
            return l_leaf
        else:
            return root
