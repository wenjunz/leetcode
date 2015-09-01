import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = [(lists[i].val,lists[i]) for i in xrange(len(lists)) if lists[i] is not None]
        heapq.heapify(heap);

        while nodes:
            

