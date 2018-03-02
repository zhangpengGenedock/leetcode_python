# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

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
        offical solution: https://leetcode.com/problems/reverse-linked-list/solution/
        :type head: ListNode
        :rtype: ListNode
        """
        rev, cur = None, head
        while cur:
            rev, rev.next, cur = cur, rev, cur.next
        return rev

    def reverseListRecursive(self, head):
        """
        offical solution: https://leetcode.com/problems/reverse-linked-list/solution/
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        rev = self.reverseListRecursive(head.next)
        head.next.next = head  # Reverse the tail of new reversed to list to point to current node
        head.next = None
        return rev
