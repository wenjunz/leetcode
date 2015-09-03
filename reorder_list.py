# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return head;

        # find the mid point
        fast = head;
        slow = head;
        while fast.next and fast.next.next:
            fast = fast.next.next;
            slow = slow.next;

        # reverse second half
        head1 = slow.next;
        slow.next = None;

        n1 = head1;
        curr = None;
        while n1:
            tmp = n1.next;
            n1.next = curr;
            curr = n1;
            n1 = tmp;

        # merge two lists
        n,n1 = head,curr;
        while n1:
            tmp = n.next;
            tmp1 = n1.next
            n.next = n1;
            n1.next = tmp;
            n1 = tmp1;
            n = n.next.next

