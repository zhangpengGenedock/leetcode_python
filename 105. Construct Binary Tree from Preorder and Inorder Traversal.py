# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root

    def buildTree2(self, preorder, inorder):
        """
        https://discuss.leetcode.com/topic/21287/python-short-recursive-solution
        :param preorder:
        :param inorder:
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree2(preorder, inorder[:ind])
            root.right = self.buildTree2(preorder, inorder[ind + 1:])
            return root

    def buildTree3(self, preorder, inorder):
        """
        https://discuss.leetcode.com/topic/16221/simple-o-n-without-map/2
        Consider the example again. Instead of finding the 1 in inorder, splitting the arrays into parts and recursing
        on them, just recurse on the full remaining arrays and stop when you come across the 1 in inorder. That's what
        my above solution does. Each recursive call gets told where to stop, and it tells its subcalls where to stop.
        It gives its own root value as stopper to its left subcall and its parent`s stopper as stopper to its right subcall.
        :param preorder:
        :param inorder:
        :return:
        """

        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.reverse()
        return build(None)
