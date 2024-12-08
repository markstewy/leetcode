class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i, n in enumerate(nums):
            while dq and n > dq[-1]["n"]:
                dq.pop()
            
            dq.append({"idx": i, "n": n})

            lastValidIdx = i - k + 1

            while dq and dq[0]["idx"] < lastValidIdx:
                dq.popleft()
            
            if lastValidIdx >= 0:
                ans.append(dq[0]["n"])
        
        return ans
