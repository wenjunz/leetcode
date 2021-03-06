# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorder_iter(root)
        
    def inorder_iter(self,root):
        stack =  []
        l = []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                l.append(root.val)
                root = root.right
        return l
