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
            dq.append(head)
            head = head.next
            dq[-1].next = None
        
        dhead = ListNode()
        curr = dhead

        while dq:
            curr.next = dq.popleft()
            curr = curr.next
            if curr:
                curr.next = dq.pop() if dq else None
                curr = curr.next
        
        return dhead.next

