# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dhead = ListNode()
        dhead.next = head

        l, r = dhead, dhead
        i = 0

        while r.next:
            r = r.next
            if i >= n:
                l = l.next
            i += 1
        
        l.next = l.next.next if l.next else None
    
        return dhead.next

