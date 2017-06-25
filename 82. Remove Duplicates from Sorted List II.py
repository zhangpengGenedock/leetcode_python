# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        https://discuss.leetcode.com/topic/21369/python-in-place-solution-with-dummy-head-node
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next

    def deleteDuplicates2(self, head):
        """
        比较符合直觉的解法
        https://discuss.leetcode.com/topic/33322/share-beat-100-python-code
        :param head:
        :return:
        """
        dummy = ListNode(0)
        pt = dummy
        repeated = 0
        while head and head.next:
            if head.val != head.next.val:
                if not repeated:
                    pt.next = head
                    pt = pt.next
                repeated = 0
            else:
                repeated = 1
            head = head.next
        pt.next = None if repeated else head
        return dummy.next
