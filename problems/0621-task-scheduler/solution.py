class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # execute the highest freq tasks first
        # use a que to set aside a task during it's gap time
        maxheap = [-v for v in Counter(tasks).values()]
        heapq.heapify(maxheap)
        timeout = deque() #[time, taskcount]
        time = 0

        while maxheap or timeout:
            time += 1

            while timeout and timeout[0][0] < time:
                taskCount = timeout.popleft()[1]
                heapq.heappush(maxheap, taskCount)
            
            if not maxheap:
                time = timeout[0][0]
            else:
                task = heapq.heappop(maxheap) + 1
                if task < 0:
                    timeout.append([time + n, task])
        
        return time
            

