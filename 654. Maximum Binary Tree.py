# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        https://discuss.leetcode.com/topic/98419/concise-python-solution-with-explanation
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        i = nums.index(max(nums))
        node = TreeNode(nums[i])
        node.left = self.constructMaximumBinaryTree(nums[:i])
        node.right = self.constructMaximumBinaryTree(nums[i + 1:])
        return node


    def constructMaximumBinaryTree2(self, nums):
        """
        fastest iterative submission
        :param nums:
        :return:
        """
        stack = []
        for i in range(len(nums)):
            curr = TreeNode(nums[i])
            while stack and stack[-1].val < nums[i]:
                curr.left = stack.pop()
            if stack:
                stack[-1].right = curr
            stack.append(curr)
        return stack[0]
