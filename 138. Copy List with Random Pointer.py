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
