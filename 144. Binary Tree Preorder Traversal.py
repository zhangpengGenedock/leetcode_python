"""
https://leetcode.com/problems/binary-tree-preorder-traversal/description/

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        recursive solution
        :type root: TreeNode
        :rtype: List[int]
        """

        def helper(root, result):
            if not root:
                return
            result.append(root.val)
            helper(root.left, result)
            helper(root.right, result)

        result = []
        helper(root, result)
        return result

    def preorderTraversal2(self, root):
        """
        https://discuss.leetcode.com/topic/7976/very-simple-iterative-python-solution
        :param root:
        :return:
        """
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return ret
