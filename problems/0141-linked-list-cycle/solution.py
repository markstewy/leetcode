# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = []

        while head:
            if id(head) in nodes:
                return True
            else:
                nodes.append(id(head))
            head = head.next
        
        return False
