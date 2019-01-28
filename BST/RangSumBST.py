# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.sum = 0
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def inorder(root):
            if root:
                inorder(root.left)
                if root.val<=R and root.val>=L:
                    self.sum+=root.val
                inorder(root.right)
        inorder(root)
        return self.sum
    
    def rangeSumBST2(self, root, L, R):
        #dfs method
        def dfs(node):
            if node:
                if L<=node.val<=R:
                    self.sum+=node.val
                    dfs(node.left)
                    dfs(node.right)
                if node.val<L:
                    dfs(node.right)
                if node.val>R:
                    dfs(node.left)
        dfs(root)
        return self.sum



            
            