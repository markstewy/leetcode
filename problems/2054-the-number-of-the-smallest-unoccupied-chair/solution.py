class Solution:
            
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # seats are 0 to len(times) max will be every seated at same time
        availableSeatIds = list( range(len(times)) ) # minheap
        minHeap = heapq.heapify(availableSeatIds)

        chrono = [] # {"friend": 0, "time": 0, "action": leave/arr}
        assignedSeats = {} # friendId: seatTaken 

        for i, t in enumerate(times):
            chrono.append({"friend": i, "time": t[0], "action": "arrive"})
            chrono.append({"friend": i, "time": t[1], "action": "leave"})

        chrono.sort(key= lambda x: x["action"], reverse=True) # so that time ties will have leave happen first
        chrono.sort(key= lambda x: x["time"])

        for event in chrono:
            if event["action"] == "arrive":
                seat = heapq.heappop(availableSeatIds)
                if event["friend"] == targetFriend:
                    return seat
                assignedSeats[event["friend"]] = seat

            elif event["action"] == "leave":
                seat = assignedSeats[event["friend"]]
                heapq.heappush(availableSeatIds, seat)

        return -1




