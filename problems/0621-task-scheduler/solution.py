class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # max count tasks on max heap
        # dq to hold waiting tasks

        maxHeap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(maxHeap)
        waitQueue = deque()

        interval = 0

        while maxHeap or waitQueue:
            interval += 1

            if waitQueue and waitQueue[0]["time"] < interval:
                heapq.heappush(maxHeap, waitQueue[0]["cnt"])
                waitQueue.popleft()

            if maxHeap:
                jobCount = heapq.heappop(maxHeap) + 1
                if jobCount:
                    waitQueue.append({"cnt": jobCount, "time": interval + n})

        return interval
