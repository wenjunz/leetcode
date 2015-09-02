# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1,l2 = True,True;
        
        nA,nB = headA,headB
        while nA and nB:
            if nA is nB: return nA
            nA = nA.next;
            nB = nB.next;
            
            if nA is None and l1:
                nA = headB;
                l1 = False;
            if nB is None and l2:
                nB = headA;
                l2 = False;
        return None   
