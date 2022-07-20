# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def sortNode(ListNode):
            return ListNode.val
    
        if len(lists) == 0:
            return None
        
        nodeArray: List[ListNode] = []
        for list in lists:
            while list:
                nodeArray.append(ListNode(list.val))
                list = list.next
                
        sortedNodeArray = sorted(nodeArray, key=sortNode)
        rootNode = sortedNodeArray[0] if len(sortedNodeArray) > 0 else None
        
        for i, x in enumerate(sortedNodeArray):
            if i < len(sortedNodeArray) - 1:
                sortedNodeArray[i].next = sortedNodeArray[i + 1]
        
        return rootNode