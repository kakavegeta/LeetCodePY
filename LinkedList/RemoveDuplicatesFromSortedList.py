class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None
        if not head.next:
            return head 
        prev, cur = None, head
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return head

