# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second and remove node linking first and second half
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        
        lHead = head
        rHead = prev

        while rHead:
            tempNextL, tempNextR = lHead.next, rHead.next
            lHead.next = rHead
            rHead.next = tempNextL
            lHead = tempNextL
            rHead = tempNextR
        
        return head

