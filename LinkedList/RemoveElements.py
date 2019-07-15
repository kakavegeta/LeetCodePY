class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        fakeHead = ListNode(None)
        fakeHead.next = head
        prev, cur = fakeHead, head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return fakeHead.next
    
    def removeElements2(self, head, val):
        if not head:
            return None
        head.next = self.removeElements2(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head
