# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        n = len(preorder)
        return self.build(preorder,inorder,0,n-1,0,n-1)
    
    def build(self,preorder,inorder,p1,p2,i1,i2):
        if i1>i2:
            return None
        else:
            val = preorder[p1]
            i0 = inorder.index(val)
            root = TreeNode(val)
            n_left,n_right = i0-i1,i2-i0
            root.left = self.build(preorder,inorder,p1+1,p1+n_left,i1,i1+n_left-1)
            root.right = self.build(preorder,inorder,p1+1+n_left,p2,i0+1,i2)
            return root
