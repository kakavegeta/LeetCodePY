class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        new_head = tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length+=1
        tail.next = head
        if k%length:
            for _ in range(length-k%length):
                tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head
            



