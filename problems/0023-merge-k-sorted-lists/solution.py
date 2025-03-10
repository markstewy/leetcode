# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        heapq.heapify(minHeap)
        nodeMap = collections.defaultdict(list)

        for curr in lists:
            while curr:
                heapq.heappush(minHeap, curr.val)
                nodeMap[curr.val].append(curr)
                temp = curr
                curr = curr.next
                temp.next = None
    
        dhead = ListNode()
        curr = dhead
        while minHeap:
            val = heapq.heappop(minHeap)
            curr.next = nodeMap[val].pop()
            curr = curr.next
        
        return dhead.next
