"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        orgToCopy = {}

        dhead = Node(-1)
        dhead.next = head

        while head:
            orgToCopy[id(head)] = Node(head.val)
            head = head.next

        head = dhead.next
        cpyHead = Node(-1)
        cpy = cpyHead
        
        while head:
            cpy.next = orgToCopy[id(head)]
            cpy = cpy.next
            cpy.random = orgToCopy[id(head.random)] if head.random else None
            head = head.next

        return cpyHead.next




