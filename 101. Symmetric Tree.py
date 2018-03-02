# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
https://leetcode.com/problems/symmetric-tree/description/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.


"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        讲解不错
        offical solution: https://leetcode.com/problems/symmetric-tree/solution/
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_mirror(root, root)

    def is_mirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.val == t2.val) and self.is_mirror(t1.right, t2.left) and self.is_mirror(t1.left, t2.right)

    def isSymmetric2(self, root):
        from collections import deque
        q = deque()
        q.append(root)
        q.append(root)
        while len(q) > 0:
            t1 = q.popleft()
            t2 = q.popleft()
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True
