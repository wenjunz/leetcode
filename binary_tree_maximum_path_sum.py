# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mem = {}
        self.maxpath(root,mem)
        m = None
        for n,val in mem.items():
            m = max(m,sum(val)-n.val)
        return m
        
    def maxpath(self,root,mem={}):
        if not root:
            return [0,0]
        if root in mem:
            return mem[root]
        else:
            mem[root] = [root.val+max(max(self.maxpath(root.left,mem)),0),\
                        root.val+max(max(self.maxpath(root.right,mem)),0)]
            return mem[root]
