class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chrono = []
        minSeats = list(range(len(times) + 1))
        heapq.heapify(minSeats)
        friendToSeat = {}

        for friend, (arrTime, leaveTime) in enumerate(times):
            chrono.append([arrTime, "2arrive", friend])
            chrono.append([leaveTime, "1leave", friend]) # leave first
        
        chrono.sort()

        for arrTime, typ, friend in chrono:
            if friend == targetFriend:
                return heapq.heappop(minSeats)
            if typ == "1leave":
                seat = friendToSeat[friend]
                heapq.heappush(minSeats, seat)
                del friendToSeat[friend]
            if typ == "2arrive":
                seat = heapq.heappop(minSeats)
                friendToSeat[friend] = seat
            

        

        


