class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        endTimes = []
        heapq.heapify(endTimes)
        intervals.sort()
        maxRooms = 0

        for s, e in intervals:
            while endTimes and endTimes[0] <= s:
                heapq.heappop(endTimes)
            
            heapq.heappush(endTimes, e)
            maxRooms = max(maxRooms, len(endTimes))
        
        return maxRooms



