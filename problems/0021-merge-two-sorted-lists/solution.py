# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ansHead = ListNode()
        curr = ansHead


        while list1 or list2:
            l1val = list1.val if list1 else float("infinity")
            l2val = list2.val if list2 else float("infinity")
        
            if l1val <= l2val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
                curr.next = None
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
                curr.next = None
        
        return ansHead.next
