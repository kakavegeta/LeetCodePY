"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def pre_order(root, res=[]):
            if root:
                res.append(root.val)
                for c in root.children:
                    pre_order(c)
            return res
        return pre_order(root)
    
    def preorder2(self, root):
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for c in node.children[::-1]:
                stack.append(c)
        return res