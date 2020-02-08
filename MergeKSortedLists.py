class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

head1 = ListNode(1)
cur1 = head1
head1.next = ListNode(4)
head1 = head1.next
head1.next = ListNode(5)

head2 = ListNode(1)
cur2 = head2
head2.next = ListNode(3)
head2 = head2.next
head2.next = ListNode(4)

res = [cur1,cur2]

def getEle(lN):
    stack = []
    while lN != None:
        stack.append(lN.val)
        lN = lN.next
    return stack

def goGood(res):
    total = []
    for i in res:
        total = total + getEle(i)
    return sorted(total)

def ListToListNode(l1):
    header = ListNode(l1[0])
    cur = header
    for i in range(1,len(l1)):
        header.next = ListNode(l1[i])
        header = header.next
    return cur

print(ListToListNode(goGood(res)))




































































