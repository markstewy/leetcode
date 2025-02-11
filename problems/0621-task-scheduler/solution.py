class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = [-c for c in Counter(tasks).values()]
        heapq.heapify(taskCounts) # maxheap of task (task with highest count has priority)
        timeout = deque() # (time, count)

        time = 0
        while taskCounts or timeout:
            time += 1

            while timeout and timeout[0][0] < time:
                heapq.heappush(taskCounts, timeout.popleft()[1])
            
            if taskCounts:
                taskCount = heapq.heappop(taskCounts) + 1
                if taskCount != 0:
                    timeout.append((time + n, taskCount))
            if timeout and not taskCounts:
                time = timeout[0][0]
        
        return time
            


        


