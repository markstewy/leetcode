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
        dhead = Node(-1)
        orgToCpy = {}

        org = head
        cpy = dhead

        while org:
            cpy.next = Node(org.val)
            orgToCpy[id(org)] = cpy.next

            cpy = cpy.next
            org = org.next
        
        org = head
        cpy = dhead.next

        while org:
            cpy.random = orgToCpy[id(org.random)] if org.random else None
            cpy = cpy.next
            org = org.next
        
        return dhead.next

