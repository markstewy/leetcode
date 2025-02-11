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
        
        cpydhead = Node(-1)
        cpy = cpydhead
        org = head

        while org:
            cpy.next = Node(org.val)
            orgToCopy[id(org)] = cpy.next

            cpy = cpy.next
            org = org.next
        
        org = head
        cpy = cpydhead.next

        while org:
            cpy.next = orgToCopy[id(org.next)] if org.next else None
            cpy.random = orgToCopy[id(org.random)] if org.random else None
            org = org.next
            cpy = cpy.next
        
        return cpydhead.next


