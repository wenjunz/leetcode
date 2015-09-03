# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if not head: return None;
        
        # insert new nodes in between old nodes, keep random pointer
        curr = head;
        while curr:
            tmp = curr.next;
            curr.next = RandomListNode(curr.label)
            curr.next.random = curr.random;
            curr.next.next = tmp;
            curr = tmp;
        
        # correct the random pointer of the newly inserted nodes
        curr = head;
        while curr and curr.next:
            if curr.next.random: curr.next.random = curr.random.next
            curr = curr.next.next
        
        # splite the list into two
        head_new = head.next;
        curr, curr_new = head, head_new; 

        while curr and curr.next:
            curr.next = curr.next.next
            if curr_new.next: curr_new.next = curr_new.next.next;
            
            curr = curr.next;
            curr_new = curr_new.next;

        return head_new
