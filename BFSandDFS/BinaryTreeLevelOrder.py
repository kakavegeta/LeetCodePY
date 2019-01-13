# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, queue = [], [root]
        if root == None:
            return res
        while queue:
            tmp = []
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                tmp.append(cur.val)
            res.insert(0, tmp)
        return res

class Solution2:
    def levelOrderBottom(self, root):
        '''
        DFS
        '''
        def dfs(root, level, res):
            if not root:
                return
            if level >= len(res):
                res.insert(0, [])
            res[-(level+1)].append(root.val)
            dfs(root.left, level+1, res)
            dfs(root.right, level+1, res)
        
        res = []
        dfs(root, 0, res)
        return res
