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
            temp = node.next
            node.next = copy
            copy.next = temp
            node = temp
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
        return head_head
        """
        node = head
        copy = dummy = Node(None, None, None)
        while node:
            node_temp = node.next.next
            copy_temp = node.next
            copy.next = copy_temp
            copy = copy_temp
            node.next = node_temp
            node = node_temp
        return dummy.next
        """
        
    