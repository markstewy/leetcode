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
        orgToCpy = {}
        cpyDhead = Node(-1)
        cpy = cpyDhead
        dhead = head

        while head:
            cpy.next = Node(head.val)
            cpy = cpy.next
            orgToCpy[id(head)] = cpy
            head = head.next
        
        head = dhead
        cpy = cpyDhead.next
        
        while head:
            cpy.random = orgToCpy[id(head.random)] if head.random else None
            head = head.next
            cpy = cpy.next
        
        return cpyDhead.next
