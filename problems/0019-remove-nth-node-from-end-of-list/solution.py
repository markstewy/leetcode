# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dhead = ListNode()
        dhead.next = head

        length = 0
        while head:
            length += 1
            head = head.next

        head = dhead
        target = length - n
        i = 1
        while i <= target:
            head = head.next
            i += 1

        head.next = head.next.next if head.next else None

        return dhead.next
