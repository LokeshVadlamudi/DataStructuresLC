class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p1, p2 = None, head
        while p2 != None:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        return p1








