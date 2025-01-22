class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = [-count for count in Counter(tasks).values()] # maxheap
        taskCounts.sort(reverse=True)
        
        time = 0
        heapq.heapify(taskCounts)
        dq = deque()
        
        while taskCounts or dq:
            time += 1

            # add back all items from dq if wait is over
            while dq and dq[0][0] < time:
                heapq.heappush(taskCounts, dq.popleft()[1])
            
            # execute the current task with the max count
            if not taskCounts:
                continue
            taskCount = heapq.heappop(taskCounts) + 1

            # if still counts left on that task, put back in the dq
            if taskCount:
                dq.append((time + n, taskCount))
        
        return time


            # for each time increment move add back all from timeout that are done waiting
            # operate on the largest in the maxheap
            # if it still has counts left move to timeout queue
            
            # move to queue




