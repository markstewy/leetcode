class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        mtgEnds = []
        heapq.heapify(mtgEnds)

        maxRooms = 0

        for b, e in intervals:
            while mtgEnds and mtgEnds[0] <= b:
                heapq.heappop(mtgEnds)

            heapq.heappush(mtgEnds, e)
            maxRooms = max(maxRooms, len(mtgEnds))
        
        return maxRooms
