"""
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def helper(self, root):
        if not root:
            return 0, True
        left_height, left_balanced = self.helper(root.left)
        right_height, right_balanced = self.helper(root.right)
        return max(left_height, right_height) + 1, left_balanced and right_balanced and abs(
            left_height - right_height) <= 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height, balanced = self.helper(root)
        return balanced

    def isBalanced2(self, root):

        """
        https://discuss.leetcode.com/topic/42953/very-simple-python-solutions-iterative-and-recursive-both-beat-90
        :param root: 
        """

        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1


if __name__ == '__main__':
    root = TreeNode(1)
    right1 = TreeNode(2)
    right2 = TreeNode(3)
    root.right = right1
    right1.right = right2
    print Solution().isBalanced(root)
