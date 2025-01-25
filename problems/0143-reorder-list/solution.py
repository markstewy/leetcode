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
        
        while dq:
            l = dq.popleft()
            r = dq.pop() if dq else None
            
            l.next = r
            if r:
                r.next = dq[0] if dq else None 

