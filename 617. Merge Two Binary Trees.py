# question: https://leetcode.com/problems/merge-two-binary-trees/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        offical solution: https://leetcode.com/problems/merge-two-binary-trees/solution/
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    def mergeTrees2(self, t1, t2):
        if t1 is None:
            return t2

        stack = []
        stack.append((t1, t2))
        while stack:
            l, r = stack.pop()
            if not l or not r:
                continue
            l.val += r.val
            if l.left is None:
                l.left = r.left
            else:
                stack.append((l.left, r.left))

            if l.right is None:
                l.right = r.right
            else:
                stack.append((l.right, r.right))
        return t1
