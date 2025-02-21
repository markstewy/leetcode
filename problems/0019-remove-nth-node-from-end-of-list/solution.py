# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dhead = ListNode()
        dhead.next = head
        
        count = 0
        l, r = dhead, dhead

        while r.next:
            r = r.next
            count += 1
            if count > n:
                l = l.next
        
        
        l.next = l.next.next if l.next.next else None
        return dhead.next


