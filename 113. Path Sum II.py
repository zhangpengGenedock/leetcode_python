"""
https://leetcode.com/problems/path-sum-ii/

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def helper(root, result, temp, s):
            if not root:
                return
            if not root.left and not root.right and root.val == s:
                result.append(temp + [root.val])
                return
            helper(root.left, result, temp + [root.val], s - root.val)
            helper(root.right, result, temp + [root.val], s - root.val)

        result = []
        helper(root, result, [], s)
        return result

    def pathSum2(self, root, sum):
        """
        https://discuss.leetcode.com/topic/16607/short-python-solution
        :param root: 
        :param sum: 
        :return: 
        """
        if not root:
            return []
        if not root.left and not root.right:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        a = self.pathSum2(root.left, sum - root.val) + self.pathSum2(root.right, sum - root.val)
        return [[root.val] + i for i in a]


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    print Solution().pathSum(root, 3)
