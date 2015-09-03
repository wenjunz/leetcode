# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __reverse__(self, head, new_head):
        if head is None:
            return new_head;
        next = head.next;
        head.next = new_head;
        return self.__reverse__(next, head)

    def reverseList_recursive(self, head):
        return self.__reverse__(head, None);

    def reverseList_iterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curt = None;
        while head is not None:
            temp = head.next;
            head.next = curt;
            curt = head;
            head = temp;

        return curt

    #reverseList = reverseList_iterative;
    reverseList = reverseList_recursive;
