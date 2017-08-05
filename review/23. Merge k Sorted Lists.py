# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        https://discuss.leetcode.com/topic/33609/10-line-python-solution-with-priority-queue
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        curr = dummy = ListNode(None)
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val, node))
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next

    def mergeKLists2(self, lists):
        """
        https://discuss.leetcode.com/topic/23140/108ms-python-solution-with-heapq-and-avoid-changing-heap-size
        :param lists: 
        :return: 
        """
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = curr = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h)
            else:
                heapreplace(h, (n.next.val, n.next))
            curr.next = n
            curr = curr.next
        return dummy.next
