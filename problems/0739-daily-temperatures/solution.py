class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        minheap = [] # (temp, idx)

        for i, t in enumerate(temps):
            while minheap and t > minheap[0][0]:
                idx = minheap[0][1]
                ans[idx] = i - idx
                heapq.heappop(minheap)
            
            heapq.heappush(minheap, (t, i))
        
        return ans
