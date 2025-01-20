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
        
        orgTocpy = {}

        cpyhead = Node(0)
        cpy = cpyhead
        org = head

        while org:
            cpy.next = Node(org.val)

            orgTocpy[id(org)] = cpy.next

            org = org.next
            cpy = cpy.next
        
        cpy = cpyhead.next
        org = head

        while head:
            cpy.random = orgTocpy[id(head.random)] if head.random else None

            head = head.next
            cpy = cpy.next
        
        return cpyhead.next
