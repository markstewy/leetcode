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
            return head

        orgTocpy = {}
        curr = head

        while curr:
            orgTocpy[id(curr)] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            cpy = orgTocpy[id(curr)]
            next = orgTocpy[id(curr.next)] if curr.next else None
            random = orgTocpy[id(curr.random)] if curr.random else None
            cpy.next = next
            cpy.random = random
            curr = curr.next
        
        return orgTocpy[id(head)]
