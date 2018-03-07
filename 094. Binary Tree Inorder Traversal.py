"""
https://leetcode.com/problems/binary-tree-inorder-traversal/description/

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.helper(root, result)
        return result

    def helper(self, root, result):
        if root is None:
            return
        self.helper(root.left, result)
        result.append(root.val)
        self.helper(root.right, result)

    def inorderTraversal2(self, root):
        """
        https://discuss.leetcode.com/topic/21350/python-recursive-and-iterative-solutions/2
        :param root:
        """
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right


if __name__ == '__main__':
    Solution().inorderTraversal()
