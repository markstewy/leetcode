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
        store = {}
        
        dhead = Node(-1)

        org = head
        cpy = dhead

        while org:
            cpy.next = Node(org.val)
            store[id(org)] = cpy.next    
            cpy = cpy.next
            org = org.next
        
        org = head
        cpy = dhead.next
        while org:
            cpy.random = store[id(org.random)] if org.random else None

            cpy = cpy.next
            org = org.next
        
        return dhead.next
        

