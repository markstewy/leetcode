class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(maxHeap)
        waitDq = deque() # {time, val}

        time = 0
        while waitDq or maxHeap:
            time += 1
            # add back all dq vales that have waited long enough to the heap
            while waitDq and waitDq[0]["time"] <= time:
                heapq.heappush(maxHeap, waitDq[0]["cnt"])
                waitDq.popleft()
            
            # take the top of the maxHeap and decrement (if any left sent to the waiting dq)
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt:
                    waitDq.append({"time": time + n + 1, "cnt": cnt})
        
        return time
