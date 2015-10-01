# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        L = []
        self.inorder(root,L)
        if len(L)<2: return True
        for i in xrange(1,len(L)):
            if L[i] <= L[i-1]: return False
        return True
        
    def inorder(self,root,L):
        if root:
            self.inorder(root.left,L)
            L.append(root.val)
            self.inorder(root.right,L)
