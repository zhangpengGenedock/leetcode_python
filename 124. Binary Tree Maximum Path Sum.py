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
            """
            the given solution deals with negative numbers just fine. the l and s variables are used to track 
            “one-side” max sum, and so initialized with zero to indicate that this one side is not being taken into 
            account (hence, it must be zero). lr and rs track the max path (that doesn’t go through the root), 
            so they are initialized with None to represent the minimum value possible (max will consider None to be 
            the lowest value possible) :param node: :return: 
            """
            l = r = 0
            ls = rs = 0
            if node.left:
                l, ls = dfs(node.left)
                l = max(l, 0)
            if node.right:
                r, rs = dfs(node.right)
                r = max(r, 0)
            return node.val + max(l, r), max(node.val + l + r, ls, rs)

        if root:
            return dfs(root)[1]
