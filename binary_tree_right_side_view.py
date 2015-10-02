# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        return self.bfs(root)
        
    def bfs(self,root):
        l = []
        frontier = [root];
        while frontier:
            l.append(frontier[-1].val)
            frontier = [[n.left,n.right] for n in frontier]
            frontier = [x for b in frontier for x in b if x]
        return l
