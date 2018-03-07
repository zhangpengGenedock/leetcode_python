"""
https://leetcode.com/problems/unique-binary-search-trees-ii/description/

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_node(val, left, right):
    node = TreeNode(val)
    node.left = left
    node.right = right
    return node


class Solution(object):
    def generateTrees(self, last, first=1):
        if last == 0:
            return []
        return [create_node(root, left, right)
                for root in range(first, last + 1)
                for left in self.generateTrees(root - 1, first)
                for right in self.generateTrees(last, root + 1)] or [None]


class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        def generate(first, last):

            trees = []
            for root in range(first, last + 1):
                for left in generate(first, root - 1):
                    for right in generate(root + 1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees += node,
            return trees or [None]

        return generate(1, n)
