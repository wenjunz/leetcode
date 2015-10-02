# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height,bal = self.height(root)
        return bal

    def height(self,root,d={},b={}):
        if not root:
            return -1,True
        if root in d:
            return d[root],b[root]
        else:
            hleft,bleft = self.height(root.left,d,b)
            hright,bright = self.height(root.right,d,b)
            d[root] = 1+max(hleft,hright)
            b[root] = bleft and bright and abs(hleft-hright)<2
            return d[root],b[root]
