# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0);
        dummy.next = head;
        prev, curr = dummy, head;
        
        while curr:
            if curr.next:
                n1 = curr.next;
                n2 = curr.next.next;
                prev.next = n1;
                n1.next = curr;
                curr.next = n2;
            prev = curr;
            curr = curr.next

        return dummy.next
