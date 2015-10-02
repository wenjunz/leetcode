# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.bfs(root)

    def bfs(self,root):
        level, L = 0, []
        if not root:
            frontier = []
        else:
            frontier = [root]

        while frontier:
            L.append([n.val for n in frontier])
            if not level&1:
                frontier = [[n.right,n.left] for n in reversed(frontier)]
            else:
                frontier = [[n.left,n.right] for n in reversed(frontier)]
            frontier = [x for b in frontier for x in b if x]
            print level,level&1
            level += 1
        return L

