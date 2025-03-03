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
        if not head:
            return None
        orgToCopy = {}

        curr = head
        while curr:
            orgToCopy[id(curr)] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            cpy = orgToCopy[id(curr)]
            cpy.next = orgToCopy[id(curr.next)] if curr.next else None
            cpy.random = orgToCopy[id(curr.random)] if curr.random else None
            curr = curr.next
        
        return orgToCopy[id(head)]

