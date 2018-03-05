"""
https://leetcode.com/problems/reverse-linked-list/description/

Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pred = None
        while head:
            curr = head
            head = head.next
            curr.next = pred
            pred = curr
        return pred

    def reverseList2(self, head):
        return self._reverse(head)

    def _reverse(self, node, pred=None):
        if not node:
            return pred
        n = node.next
        node.next = pred
        return self._reverse(n, node)
