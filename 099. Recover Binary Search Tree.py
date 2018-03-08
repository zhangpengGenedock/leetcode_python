"""
https://leetcode.com/problems/recover-binary-search-tree/

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder_iter(root):
    if root:
        for node in inorder_iter(root.left):
            yield node
        yield root
        for node in inorder_iter(root.right):
            yield node


class Solution(object):
    def recoverTree(self, root):
        """
        https://discuss.leetcode.com/topic/5326/elegant-python-code-using-yield-iterator
        
        Basic algorithm is inorder traveling the tree to find the swapped pair nodes.

        By using “yield” iterator, the traveling procedure can be very elegant.
        1 2 3 6 5 4
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        pred, first = None, None
        for node in inorder_iter(root):
            if pred and pred.val > node.val:
                if first is None:
                    first = pred
                    second = node
                else:
                    second = node
                    break
            pred = node
        first.val, second.val = second.val, first.val
