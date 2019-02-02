# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root, leaves=[]):
            if root:
                if not root.left and not root.right:
                    leaves.append(root.val)
                dfs(root.left, leaves)
                dfs(root.right, leaves)
        leaves1, leaves2 = [], []
        dfs(root1,leaves1)
        dfs(root2, leaves2)
        return leaves1==leaves2