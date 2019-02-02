"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""class Solution:
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        recursion
        """
        if not root:
            return 0
        elif root.children == []:
            return 1
        else:
            h = [self.maxDepth(c) for c in root.children if c] 
            return max(h) + 1
    
    def maxDepth2(self, root):
        if not root:
            return 0
        stack = [(1, root)]
        depth = 0
        while stack:
            cur, node = stack.pop()
            if not node:
                depth = max(depth, cur)
                for c in node.children:
                    stack.append((cur+1, c))
        return depth



