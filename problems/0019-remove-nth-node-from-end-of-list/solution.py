# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dhead = ListNode()
        dhead.next = head
        left, right = dhead, dhead

        i = 0
        while right.next:
            right = right.next
            if i >= n:
                left = left.next
            i += 1
        
        left.next = left.next.next if left.next else None
    
        return dhead.next

