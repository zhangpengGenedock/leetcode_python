"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        https://discuss.leetcode.com/topic/21363/python-solutions-dfs-stack-bfs-queue-dfs-recursively
        :type root: TreeNode
        :rtype: int
        """

        # def dfs(root, result, temp):
        #     if not root.left and not root.left:
        #         result.append(temp)
        #         return
        #     if root.left:
        #         dfs(root.left, result, temp + [root.val])
        #     else:
        #         result.append(temp)
        #     if root.right:
        #         dfs(root.right, result, temp + [root.val])
        #     else:
        #         result.append(temp)
        #
        # if not root:
        #     return 0
        # result = []
        # dfs(root, result, [root.val])
        # return sum(int("".join(str(v) for v in path)) for path in result if path)

        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, val):
        if root:
            self.dfs(root.left, 10 * val + root.val)
            self.dfs(root.right, 10 * val + root.val)
            if not root.left and not root.right:
                self.res += val * 10 + root.val

    def sumNumbers1(self, root):
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.right:
                    stack.append((node.right, value * 10 + node.right.val))
                if node.left:
                    stack.append((node.left, value * 10 + node.left.val))
        return res
