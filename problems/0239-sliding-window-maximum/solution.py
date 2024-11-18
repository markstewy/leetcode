class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i, n in enumerate(nums):
            while dq and n > dq[-1]["val"]:
                dq.pop()
            
            dq.append({"val": n, "idx": i})

            lastValidIdxInWindow = i - k  + 1
            while dq and dq[0]["idx"] < lastValidIdxInWindow:
                dq.popleft()
            
            if lastValidIdxInWindow >= 0:
                ans.append(dq[0]["val"])
        
        return ans
