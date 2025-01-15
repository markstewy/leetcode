class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tCount = [-count for count in Counter(tasks).values()]
        heapq.heapify(tCount)
        
        waitq = deque() # (interval, count)
        interval = 0

        while tCount or waitq:
            interval = interval + 1

            while waitq and interval - waitq[0][0] > n:
                count = waitq.popleft()[1]
                heapq.heappush(tCount, count)
            
            if tCount:
                count = heapq.heappop(tCount)
                if count < -1:
                    waitq.append((interval, count + 1))
        
        return interval


        
        

        return 0
