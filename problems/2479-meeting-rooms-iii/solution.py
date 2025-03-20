class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        roomCount = {}

        mtgRoom = {n: 0 for n in range(n)}
        roomHeap = [n for n in range(n)]
        heapq.heapify(roomHeap) # room
        
        meetings.sort()
        meetingsDq = deque(meetings)
        endHeap = []
        heapq.heapify(endHeap) # (endTime, room)
        currTime = 0

        while meetingsDq:
            if currTime > meetingsDq[0][0]:
                mtgLen = meetingsDq[0][1] - meetingsDq[0][0]
                meetingsDq[0][0] = currTime
                meetingsDq[0][1] = currTime + mtgLen
            else:
                currTime = meetingsDq[0][0]

            # while endHeap end time <= meetingsDq[0]start time, pop end time and return to room heap
            while endHeap and endHeap[0][0] <= currTime:
                t, r = heapq.heappop(endHeap)
                heapq.heappush(roomHeap, r)

            # if room not available set the start time to endHeap time and move the end time back
            if not roomHeap:
                nextAvailTime = endHeap[0][0]
                mtgLen = meetingsDq[0][1] - meetingsDq[0][0]
                meetingsDq[0][0] = nextAvailTime
                meetingsDq[0][1] = nextAvailTime + mtgLen
                currTime = nextAvailTime

                # while endHeap end time <= meetingsDq[0]start time, pop end time and return to room heap
                while endHeap and endHeap[0][0] <= meetingsDq[0][0]:
                    t, r = heapq.heappop(endHeap)
                    heapq.heappush(roomHeap, r)
            
            # take lowest room add to end time
            r = heapq.heappop(roomHeap)
            e = meetingsDq[0][1]
            meetingsDq.popleft()
            heapq.heappush(endHeap, (e, r))
            roomCount[r] = roomCount.get(r, 0) - 1
        
        rooms = [(c, r) for r, c in roomCount.items()]
        rooms.sort()
        return rooms[0][1]
