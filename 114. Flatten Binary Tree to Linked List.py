"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    pre = None

    def flatten(self, root):
        """
        https://discuss.leetcode.com/topic/10606/an-inorder-python-solution
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.prev = root
        self.flatten(root.left)
        temp = root.right
        root.right, root.left = root.left, None
        self.prev.right = temp
        self.flatten(temp)

    def __init__(self):

        """
        https://discuss.leetcode.com/topic/33192/8-lines-of-python-solution-reverse-preorder-traversal
        confused but beautiful
        """
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


if __name__ == '__main__':
    root = TreeNode(1)
    right = TreeNode(2)
    root.right = right
    print Solution().flatten(root)
