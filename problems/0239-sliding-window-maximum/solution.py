class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i, n in enumerate(nums):
            while dq and dq[-1]["n"] < n:
                dq.pop()
            dq.append({"i": i, "n": n})

            while dq[0]["i"] <= i - k:
                dq.popleft()
            
            if i >= k - 1:
                ans.append(dq[0]["n"])
        
        return ans
