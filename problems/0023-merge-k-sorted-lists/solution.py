# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodeArr = []

        for l in lists:
            curr = l
            while curr:
                nodeArr.append(curr)
                temp = curr.next
                curr.next = None
                curr = temp
        
        nodeArr.sort(key=lambda x : x.val)

        dhead = ListNode()
        curr = dhead

        for node in nodeArr:
            curr.next = node
            curr = curr.next
        
        return dhead.next

