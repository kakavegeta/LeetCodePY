# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return
        parent, level ={root:None}, {root:0}
        frontier = [root]
        i = 1
        while frontier:
            next = []
            for u in frontier:
                for v in [u.left, u.right]:
                    if v not in level and v is not None:
                        level[v] = i
                        parent[v] = u
                        next.append(v)
            if next == []:
                return frontier[0].val
            else:
                frontier = next
                i += 1

class Solution2:
    def findBottomLeftValue(self, root):
        if root is None:
            return 
        queue = [root]
        for node in queue:
            queue += filter(None, [node.right, node.left])
            print(queue)
        return node.val

        