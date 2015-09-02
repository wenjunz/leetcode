# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head;
        if fast is None: return None;
        elif fast.next is None: return None;
        elif fast.next.next is None: return None;
        
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next;
            slow = slow.next;
            
            if fast is slow:
                fast = head;
                while fast is not slow:
                    fast = fast.next;
                    slow = slow.next;
                return fast 
        return None

