"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        https://discuss.leetcode.com/topic/26402/5-6-lines-fast-python-solution-48-ms
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans


class Solution(object):
    def __init__(self):
        self.l = []

    def helper(self, root, level):
        if not root:
            return None
        else:
            if level < len(self.l):
                self.l[level].append(root.val)
            else:
                self.l.append([root.val])
            self.helper(root.left, level + 1)
            self.helper(root.right, level + 1)
        return self.l

    def levelOrder(self, root):
        if not root:
            return []
        return self.helper(root, 0)
