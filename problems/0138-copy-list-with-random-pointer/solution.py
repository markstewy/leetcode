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
        orgToCpy = {} # key: id(org) value: pointer to cpy obj
        dhead = Node(-1)

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
            if org.random:
                cpy.random = orgToCpy[id(org.random)]
            else:
                cpy.random = None
            org = org.next
            cpy = cpy.next
        self.printlist(dhead.next)
        return dhead.next


    def printlist(self, head):
        s = ""
        while head:
            s += "val:" + str(head.random) + " "
            head = head.next
        print(s)

