
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# one pass
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first,second = dummy, dummy
        for _ in range(n):
            first = first.next
        if not first:
            return dummy.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

sol = Solution()