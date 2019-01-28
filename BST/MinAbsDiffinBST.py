class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution:
    def __init__(self):
        self.res = float('inf')
        self.pre = -float('inf')

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        inorder traversal
        """
        if root:
            self.getMinimumDifference(root.left)
            if root.val:
                self.res = min(self.res, root.val - self.pre)
            self.pre = root.val
            self.getMinimumDifference(root.right)
        return self.res
        

if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(None)
    root.right = TreeNode(2236)
    root.right.left = TreeNode(1277)
    root.right.left.left = TreeNode(519)
    root.right.right = TreeNode(2776)
    sol = Solution()
    res = sol.getMinimumDifference(root)
    print(res)