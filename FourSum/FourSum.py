class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode("")
        dummy.next = head
        start = head
        length = 0
        while start != None:
            start = start.next
            length += 1
        length = length - n
        start = dummy
        while length>0:
            length-=1
            start = start.next
        start.next = start.next.next
        return dummy.next 
