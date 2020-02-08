class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if headA == None or headB == None:
            return None
        ap = headA
        bp = headB

        acount = 0
        bcount = 0

        while (True):

            if ap == bp:
                return ap
            if ap != None:
                ap = ap.next
            else:
                ap = headB
                acount += 1
            if bp != None:
                bp = bp.next
            else:
                bp = headA
                bcount += 1

            if acount == 2 and bcount == 2:
                return None


        # p1, p2 = None, head
        # while p2 != None:
        #     p3 = p2.next
        #     p2.next = p1
        #     p1 = p2
        #     p2 = p3
        # return p1








