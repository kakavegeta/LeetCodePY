class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head.next:
            return True
        slow, fast = head, head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            # omg!
            rev, rev.next = slow, rev
            slow = slow.next
        # odd nodes
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev

