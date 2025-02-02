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
        dq = deque()

        while head:
            temp = head
            dq.append(head)
            head = head.next
            temp.next = None
        
        dhead = ListNode()
        head = dhead

        while dq:
            head.next = dq.popleft() if dq else None
            head = head.next
            head.next = dq.pop() if dq else None
            head = head.next
        
        return dhead.next

            
