class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        seats = list(range(len(times)))
        heapq.heapify(seats)
        seatMap = {} # userId: seatIdx

        events = []
        for personId, times in enumerate(times):
            events.append([times[0], "arrive", personId])
            events.append([times[1], "leave", personId])
        events.sort(key=lambda x : (-x[0], x[1]), reverse=True)

        for e in events:
            userId = e[2]

            if userId == targetFriend:
                return seats[0]
            elif e[1] == "arrive":
                seatMap[userId]  = heapq.heappop(seats)
            elif e[1] == "leave":
                heapq.heappush(seats, seatMap[userId])
                del seatMap[userId]
        
        return -1
            






