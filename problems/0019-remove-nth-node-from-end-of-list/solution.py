# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dhead = ListNode()
        dhead.next = head

        l = dhead
        r = dhead
        i = 0

        while r.next:
            i += 1
            r = r.next
            if i > n:
                l = l.next

        
        l.next = l.next.next if l.next else None
        self.printList(dhead)

        return dhead.next

    def printList(self, head):
        s = ""
        while head:
            s += str(head.val) + "--> "
            head = head.next
        
        print(s)
