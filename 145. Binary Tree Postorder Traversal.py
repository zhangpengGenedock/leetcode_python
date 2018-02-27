"""
https://leetcode.com/problems/binary-tree-postorder-traversal/description/

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3
 

return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?


"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def helper(root, result):
            if not root:
                return
            helper(root.left, result)
            helper(root.right, result)
            result.append(root.val)

        result = []
        helper(root, result)
        return result

    def postorderTraversal2(self, root):
        """
        https://discuss.leetcode.com/topic/17540/share-my-two-python-iterative-solutions-post-order-and-modified-preorder-then-reverse/2
        :param root:
        :return:
        """
        traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    traversal.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return traversal

    def postorderTraversal3(self, root):
        """
        https://discuss.leetcode.com/topic/17540/share-my-two-python-iterative-solutions-post-order-and-modified-preorder-then-reverse/2
        :param root:
        :return:
        """
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return traversal[::-1]
