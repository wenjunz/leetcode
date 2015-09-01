import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = [(lists[i].val,lists[i]) for i in xrange(len(lists)) if lists[i] is not None]
        heapq.heapify(heap);

        head = ListNode(None);
        node = head;
        while heap:
            pop = heapq.heappop(heap);
            curr.next = pop[1];
            curr = curr.next;
            if curr.next:
                heapq.heappush(heap,(curr.next.val,curr.next))
        return head.next


