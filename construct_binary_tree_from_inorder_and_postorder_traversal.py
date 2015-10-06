# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        return self.build(inorder,postorder,0,n-1,0,n-1)
        
    def build(self,inorder,postorder,i1,i2,p1,p2):
        if i2<i1:
            return None
        else:
            val = postorder[p2]
            i0 = inorder.index(val)
            root = TreeNode(val)
            n_left,n_right = i0-i1,i2-i0
            root.left = self.build(inorder,postorder,i1,i1+n_left-1,p1,p1+n_left-1)
            root.right = self.build(inorder,postorder,i0+1,i0+n_right,p1+n_left,p2-1)
            return root
