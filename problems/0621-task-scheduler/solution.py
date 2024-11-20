class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            # move from q back to heap
            while q and q[0][0] < time:
                heapq.heappush(maxHeap, q[0][1])
                q.popleft()

            # move from heap to q
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([time + n, cnt])
            else:
                time = q[0][0]


        return time
