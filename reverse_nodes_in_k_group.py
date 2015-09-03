# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # find out the length
        L = 0
        curr = head;
        while curr:
            curr = curr.next;
            L+=1;
        
        dummy = ListNode(None);
        dummy.next = head;
        prev,curr = dummy,head;
        
        while L >= k:
            tail = curr;
            for i in range(k): tail = tail.next;
            newcurr = tail;
            newprev = curr;
            
            for i in range(k):
                tmp = curr.next;
                curr.next = tail;
                tail = curr;
                curr = tmp;
            prev.next = tail;
            
            curr = newcurr;
            prev = newprev;
            
            # reverse k nodes following n
            # advance k nodes
            L-=k;
        return dummy.next
            
        
