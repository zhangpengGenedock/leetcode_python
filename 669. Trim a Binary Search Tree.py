# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its 
elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new 
root of the trimmed binary search tree. 

Example 1:
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2
Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def trimBST(self, root, L, R):
        """
        space o(N)
        time o(N)
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
