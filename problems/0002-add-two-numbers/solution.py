# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ansHead = ListNode()
        curr = ansHead

        carry = 0
        while l1 or l2 or carry:
            curr.next = ListNode()
            curr = curr.next

            l1 = l1 if l1 else ListNode()
            l2 = l2 if l2 else ListNode()

            total = l1.val + l2.val + carry
            carry = total // 10
            total = total % 10
            curr.val = total

            l1 = l1.next
            l2 = l2.next
        
        return ansHead.next
