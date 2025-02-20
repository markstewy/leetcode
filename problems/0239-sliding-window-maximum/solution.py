class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i, n in enumerate(nums):
            while dq and dq[-1]["n"] <= n:
                dq.pop()
            dq.append({"n": n, "i": i})

            lastIdx = i - k + 1
            while dq and dq[0]["i"] < lastIdx:
                dq.popleft()
            
            if i + 1 >= k:
                ans.append(dq[0]["n"])
        
        return ans
