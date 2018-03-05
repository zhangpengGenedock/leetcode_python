"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, node):
        """
        https://discuss.leetcode.com/topic/27792/ac-python-o-1-space-solution-12-lines-and-easy-to-understand
        :param node:
        """
        tail = dummy = TreeLinkNode(0)
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next

    def connect2(self, root):
        """
        https://discuss.leetcode.com/topic/9735/just-convert-common-bfs-solution-to-o-1-space-a-simple-python-code/2
        :param root:
        :return:
        """
        if not root:
            return
        queue, nextLevel = [root], []
        while queue:
            curr = queue.pop(0)
            if curr.left:
                nextLevel.append(curr.left)
            if curr.right:
                nextLevel.append(curr.right)
            if queue:
                curr.next = queue[0]
            if not queue and nextLevel:
                queue, nextLevel = nextLevel, queue
