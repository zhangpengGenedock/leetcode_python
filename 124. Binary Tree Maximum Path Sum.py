"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along 
the parent-child connections. The path must contain at least one node and does not need to go through the root. 

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.


"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            # returns: max one side path sum, max path sum
            l = r = 0
            ls = rs = None
            if node.left:
                l, ls = dfs(node.left)
                l = max(l, 0)
            if node.right:
                r, rs = dfs(node.right)
                r = max(r, 0)
            return node.val + max(l, r), max(node.val + l + r, ls, rs)

        if root:
            return dfs(root)[1]
