class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reverseList(self, head):
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next
        return rev