# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pre = -float('inf')
        res = float('inf')

        if root.left:
            self.minDiffInBST(root.left)
        res = min(res, root.val-pre)
        pre = root.val
        if root.right:
            self.minDiffInBST(self.right)
        return res
       