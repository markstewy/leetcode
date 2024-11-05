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
        orgToCopy = {} # key: org node id   value: pointer to copy node

        dchead = Node(-1)
        copyhead = dchead
        orghead = head

        while orghead:
            copyhead.next = Node(orghead.val)
            orgToCopy[id(orghead)] = copyhead.next
            orghead = orghead.next
            copyhead = copyhead.next
        
        copyhead = dchead.next
        orghead = head

        while orghead:
            if orghead.random:
                copyhead.random = orgToCopy[id(orghead.random)]
            orghead = orghead.next
            copyhead = copyhead.next
        
        return dchead.next
            

