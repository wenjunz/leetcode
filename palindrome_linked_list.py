# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def create_head(L):
    head = ListNode(None);
    node = head;
    for l in L:
        node.next = ListNode(l);
        node = node.next;
    return head.next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None : return True

        # find mid node
        fast,slow = head,head;

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next;
            slow = slow.next

        # reverse rhead
        rhead = slow.next;
        curt = None;
        while rhead is not None:
            temp = rhead.next
            rhead.next = curt;
            curt = rhead;
            rhead = temp;

        # compare
        p1,p2 = head, curt;
        while p2 is not None:
            if p1.val != p2.val: return False
            p1,p2 = p1.next, p2.next;

        return True
