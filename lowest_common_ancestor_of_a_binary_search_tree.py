# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path_p = self.find_path(root,p)
        path_q = self.find_path(root,q)
        x = 0
        while x<min(len(path_p),len(path_q)) and path_p[x] == path_q[x]:
            x+=1
        return path_p[x-1]
        
    def find_path(self,root,target):
        # base case
        if not root: return None;
        if root is target: return [target]
            
        for i in [root.left,root.right]:
            tail = self.find_path(i,target)
            if tail:
                return [root]+tail
        return None

