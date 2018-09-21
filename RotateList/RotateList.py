class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    

class Solution:

    def rotateRight(self, head, k):
        if not head:
            return 
        dummy = ListNode(0)
        tail = dummy.next = head
        length = 0
        while tail is not None:
            tail = tail.next
            length+=1
        tail.next = head
        if k%length:
            for _ in range(length-k%length):
                tail = tail.next

        new = tail.next
        tail.next = None
        return new


sol = Solution

        