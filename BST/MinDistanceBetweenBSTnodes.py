# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.pre = -float('inf')
        self.res = float('inf')

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val-self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res
       