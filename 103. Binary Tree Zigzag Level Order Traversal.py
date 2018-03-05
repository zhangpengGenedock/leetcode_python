"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, level, flag = [], [root], 1
        while root and level:
            ans.append([node.val for node in level][::flag])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
            flag *= -1
        return ans

    def zigzagLevelOrder2(self, root):
        ans = []
        self.helper(ans, 0, root)
        return ans

    def helper(self, ans, level, root):
        if not root:
            return
        elif len(ans) <= level:
            ans.append([root.val])
        elif not level % 2:
            ans[level].extend([root.val])
        else:
            ans[level].insert(0, root.val)
        self.helper(ans, level + 1, root.left)
        self.helper(ans, level + 1, root.right)
