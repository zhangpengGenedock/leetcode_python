# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        https://discuss.leetcode.com/topic/17521/share-my-python-solution-with-detailed-explanation`
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            return None

        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next
        return head
