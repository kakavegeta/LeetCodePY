class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
    
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        node = head
        # make copy
        while node:
            copy = Node(node.val, None, None)
            copy.next = node.next
            node.next = copy
            node = copy.next
        # assign random pointer to each copy
        node = head
        while node:
            if not node.random:
                node.next.random = node.random.next
            node = node.next.next
        
        # extract copies
        node = head
        copy = copy_head = head.next
        while node:
            node.next = node = copy.next
            copy.next = copy = node and node.next
        return copy_head
 
    def copyRandomList2(self, head):
        node_map = {}
        if not head:
            return None
        cur = head
        while cur:
            node_map[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                node_map[cur].next = node_map[cur.next]
            if cur.random:
                node_map[cur].random = node_map[cur.random]
            cur = cur.next
        return node_map[head]
    