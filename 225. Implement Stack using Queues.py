# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
https://leetcode.com/problems/implement-stack-using-queues/description/

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack. pop() -- Removes the element on top of the stack. top() -- Get the top element. 
empty() -- Return whether the stack is empty. Notes: You must use only standard operations of a queue -- which means 
only push to back, peek/pop from front, size, and is empty operations are valid. Depending on your language, 
queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), 
as long as you use only standard operations of a queue. You may assume that all operations are valid (for example, 
no pop or top operations will be called on an empty stack). """


class MyStack(object):
    """
    offical solution: https://leetcode.com/problems/implement-stack-using-queues/solution/
    personal solution: https://leetcode.com/problems/implement-stack-using-queues/discuss/62516/Concise-1-Queue-Java-C++-Python
    用一个对列实现一个栈
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self._queue = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self._queue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self._queue)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
