"""
https://leetcode.com/problems/partition-list/

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        lower = pre1 = ListNode(0)
        higher = pre2 = ListNode(0)
        while head:
            if head.val < x:
                pre1.next = head
                pre1 = pre1.next
                head = head.next
                pre1.next = None
            else:
                pre2.next = head
                pre2 = pre2.next
                head = head.next
                pre2.next = None
        pre1.next = higher.next
        return lower.next

    def partition2(self, head, x):
        if not head or not head.next:
            return head
        left, right = ListNode(None), ListNode(None)
        left_cur, right_cur = left, right
        while head:
            if head.val < x:
                left_cur.next, head = head, head.next
                left_cur, left_cur.next = left_cur.next, None
            else:
                right_cur.next, head = head, head.next
                right_cur, right_cur.next = right_cur.next, None
        left_cur.next = right.next
        return left.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l2 = ListNode(1)
    l1.next = l2
    # print Solution().partition(l1, 2)
    print Solution().partition2(l1, 2)
