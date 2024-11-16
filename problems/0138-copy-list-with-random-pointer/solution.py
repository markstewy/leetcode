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
        dhead = Node(-1)

        cpy = dhead
        org = head

        while org:
            cpy.next = Node(org.val)
            orgToCpy[id(org)] = cpy.next
            org = org.next
            cpy = cpy.next
        
        org = head
        cpy = dhead.next

        while org:
            cpy.random = orgToCpy[id(org.random)] if org.random else None
            org = org.next
            cpy = cpy.next

        return dhead.next

