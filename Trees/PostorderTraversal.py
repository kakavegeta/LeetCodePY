"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        recursion
        """
        def post_order(root, res=[]):
            if root:
                for child in root.children:
                    postorder(child)
                res.append(root.val)
            return res 
        res = post_order(root)
        return res
    
    def postorder2(self, root):
        """
        iteration
        """
        if not root:
            return []
        
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if  node:
                res.append(node.val)
            for child in node.children:
                stack.append(child)
        return res
        