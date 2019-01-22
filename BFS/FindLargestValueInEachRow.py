# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        frontier = [root]
        ans = []
        while frontier:
            next = []
            Max = -float('inf')
            for u in frontier:
                if u.left:
                    next.append(u.left)
                if u.right:
                    next.append(u.right)
                Max = max(Max, u.val)
            ans.append(Max)
            frontier = next
        return ans

    def largestValues2(self, root):
        ans = []
        row = [root]
        while any(row):
            ans.append(max(u.value for u in row))
            row = [child for node in row for child in (node.left, node.right) if child]
        return ans
    
    def largestValues3(self, root):
        # dfs
        def dfs(root, res, depth):
            if not root:
                return 
            if depth == len(res):
                res.append(root.val)
            else:
                res[depth] = max(root.val, res[depth]) 
            dfs(root.left, res, depth+1)
            print(res, depth, root.val)
            dfs(root.right, res, depth+1)
            print(res,depth, root.val)
        res = []
        dfs(root, res, 0)
        return res

if __name__ == "__main__":
    sol = Solution()
    Input = [1, 3, 2, 5, 3, None, 9]
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.left = None
    root.right.right = TreeNode(9)
    print(sol.largestValues3(root))

