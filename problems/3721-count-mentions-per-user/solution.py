class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        
        events.sort(key= lambda x : (-int(x[1]), x[0]), reverse=True)
        print(events)
        users = [0] * numberOfUsers
        offlineTimes = deque()
        offlineUsers = deque()
    
        for e in events:
            cmd = e[0]
            time = int(e[1])
            validUsers = []

            if e[2] == "ALL":
                validUsers = range(len(users))
            elif e[2] == "HERE":
                while offlineTimes and offlineTimes[0] <= time:
                    offlineTimes.popleft()
                    offlineUsers.popleft()        
                for u in range(len(users)):
                    if u not in offlineUsers:
                        validUsers.append(u)
            else:
                validUsers = [int(u.lstrip("id")) for u in e[2].split(" ")]

            for u in validUsers:
                if cmd == "OFFLINE":
                    offlineTimes.append(time + 60)
                    offlineUsers.append(u)
            
                if cmd == "MESSAGE":
                    users[u] += 1
            
        return users

