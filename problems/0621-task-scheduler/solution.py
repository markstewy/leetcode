class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = [-c for c in list(Counter(tasks).values())]
        heapq.heapify(taskCount)
        waitq = deque() # (t, count)


        interval = 0

        while taskCount or waitq:
            # remove all tasks from the q that have waited long enough
            while waitq and waitq[0][0] < interval:
                heapq.heappush(taskCount, waitq.popleft()[1])

            # take one task from the heap, decrement and move to waitq
            if not taskCount:
                interval = waitq[0][0]

            if taskCount:
                task = heapq.heappop(taskCount)
                task += 1
                if task < 0:
                    waitq.append((interval + n, task))


            interval += 1
        
        return interval
        
