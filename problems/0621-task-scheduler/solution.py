class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # maxheap for next task only send to dq if more tasks await
        maxHeap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(maxHeap)

        # dq for wait
        wait = deque() # {"available": i, "count": cnt}

        i = 0
        while maxHeap or wait:
            i += 1
            # check the wait queue and add all jobs that are available back to the maxHeap
            while wait and wait[0]["available"] < i:
                heapq.heappush(maxHeap, wait[0]["count"])
                wait.popleft()
            
            # take the max job from the heap and move it to the wait queue
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    wait.append({"available": i + n, "count": cnt})
            else:
                i = wait[0]["available"]
            
        return i



