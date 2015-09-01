# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1,node2 = l1,l2;

        head = ListNode(None);
        node = head;

        while node1 and node2:
            if node1.val <= node2.val:
                node.next = node1;
                node1 = node1.next;
            else:
                node.next = node2;
                node2 = node2.next;
            node = node.next;
        if node1 is None:
            node.next = node2;
        elif node2 is None:
            node.next = node1;
        
        return head.next
