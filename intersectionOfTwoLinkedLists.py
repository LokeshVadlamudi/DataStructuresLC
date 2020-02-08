class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = []
        cur = headA
        while cur != None:
            s.append(cur.val)
            cur = cur.next
        cur1 = headB
        while cur1 != None:
            if cur1.val in s:
                return cur1
            cur1 = cur1.next
        return None