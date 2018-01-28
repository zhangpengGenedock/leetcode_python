"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    offical solution: https://leetcode.com/problems/binary-tree-right-side-view/solution/
    """

    def rightSideView(self, root):
        """
        dfs
        :type root: TreeNode
        :rtype: List[int]
        """
        rightmost_value_at_depth = dict()
        max_depth = -1
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if node is not None:
                max_depth = max(max_depth, depth)
                rightmost_value_at_depth.setdefault(depth, node.val)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]

    def rightSideView2(self, root):
        """
        bfs
        :param root:
        :return:
        """
        rightmost_value_at_depth = dict()
        max_depth = -1
        from collections import deque
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if node is not None:
                max_depth = max(max_depth, depth)
                rightmost_value_at_depth[depth] = node.val
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]

    # solution from submission
    def __init__(self):
        self.view = []

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.helper(root, 0)
        return self.view

    def helper(self, root, level):
        if root == None:
            return
        level += 1
        if len(self.view) < level:
            self.view.append(root.val)
        self.helper(root.right, level)
        self.helper(root.left, level)
