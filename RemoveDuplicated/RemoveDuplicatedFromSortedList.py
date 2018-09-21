class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = head
        while current.next is not None and current is not None::
            if current.val==current.next.val:
                current = current.next.next
            else:
                current = current.next
        return dummy.next