class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chairs = list(range(len(times)))
        heapq.heapify(chairs)

        events = []
        for name, t in enumerate(times):
            arrTime = t[0]
            depTime = t[1]
            events.append([arrTime, "2-arr", name])
            events.append([depTime, "1-dep", name])
        events.sort()

        friendSeats = {}
        for time, event, name in events:
            if event == "2-arr":
                if name == targetFriend:
                    return heapq.heappop(chairs)
                friendSeats[name] = heapq.heappop(chairs)
            if event == "1-dep":
                heapq.heappush(chairs, friendSeats[name])
                del friendSeats[name]
        
        return -1


