class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        ans = []

        for i, n in enumerate(nums):
            while len(dq) > 0 and n > dq[-1]["num"]:
                dq.pop()
            
            while len(dq) > 0 and dq[0]["idx"] <= (i - k):
                dq.popleft()
            
            dq.append({"idx": i, "num": n})
            
            if i >= k - 1:
                ans.append(dq[0]["num"])

        return ans


