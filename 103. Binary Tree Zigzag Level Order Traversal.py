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
