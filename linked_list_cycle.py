# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return False;
        fast, slow = head, head;
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next;
            slow = slow.next;
            if fast is slow: return True
        return False
