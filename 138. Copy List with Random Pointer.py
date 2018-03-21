"""
https://leetcode.com/problems/copy-list-with-random-pointer/description/

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):

        """
        {@link} 138. Copy List with Random Pointer.jpg)
        https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)
        :param head: 
        :return: 
        """

        # Insert each node's copy right after it, already copy .label
        node = head
        while node:
            copy = RandomListNode(node.label)
            copy.next = node.next
            node.next = copy
            node = copy.next

        # Set each copy's .random
        node = head
        while node:
            node.next.random = node.random and node.random.next
            node = node.next.next

        # Separate the copied list from the original, (re)setting every .next
        node = head
        copy = head_copy = head and head.next
        while node:
            # ? 未看懂 node.next = node 含义? 死循环？
            node.next = node = copy.next
            copy.next = copy = node and node.next

        return head_copy

    def copyRandomList1(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = dict()
        m = n = head
        while m:
            dic[m] = RandomListNode(m.label)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)

    def copyRandomList2(self, head):
        import collections
        dic = collections.defaultdict(lambda: RandomListNode(0))
        dic[None] = None
        n = head
        while n:
            dic[n].label = n.label
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]
