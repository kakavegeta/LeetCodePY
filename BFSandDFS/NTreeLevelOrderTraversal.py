"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        q, res = [root], []
        while any(q):
            res.append([node.val for node in q]) 
            q = [child for node in q for child in node.children if child]
        return res
