# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
https://leetcode.com/problems/binary-tree-upside-down/description/

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same 
parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf 
nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1  
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        solution: https://discuss.leetcode.com/topic/26276/explain-the-question-and-my-solution-python/2
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:
            return root
        lRoot = self.upsideDownBinaryTree(root.left)
        rMost = lRoot
        while rMost.right:
            rMost = rMost.right
        root, rMost.left, rMost.right = lRoot, root.right, TreeNode(root.val)
        return root
