class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = [[-count, task] for task, count in Counter(tasks).items()]

        waitq = deque()
        heapq.heapify(maxheap)
        interval = 0

        while waitq or maxheap:
            interval += 1

            while waitq and waitq[0][0] < interval:
                heapq.heappush(maxheap, waitq.popleft()[1])
                print(maxheap[0])
            
            if maxheap:
                task = heapq.heappop(maxheap)
                task[0] += 1
                if task[0] < 0:
                    waitq.append([interval + n, task]) # [n, [c, a]]
        
        return interval
