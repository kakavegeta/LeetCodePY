# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        BFS
        """
        def isMirror(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None and root2 is not None:
                return False
            if root1 is not None and root2 is None:
                return False
            return root1.val == root2.val and isMirror(root1.left, root2.right) and isMirror(root2.left, root1.right)
        
        return isMirror(root, root)

class Solution2:
    def isSymmetric(self, root):
        queue = [root, root]
        while queue:
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True

