# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        stack = [(t1, t2)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 or not node2:
                continue
            node1.val += node2.val
            if not node1.left:
                node1.left = node2.left
            else:
                stack.append((node1.left, node2.left))
            if not node1.right:
                node1.right = node2.right
            else:
                stack.append((node1.right, node2.right))
        return t1

