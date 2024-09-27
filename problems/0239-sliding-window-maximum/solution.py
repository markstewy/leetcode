class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i, n in enumerate(nums):
            while dq and n > dq[-1]["val"]:
                dq.pop()
            
            dq.append({"val": n, "idx": i})
            

            if i >= k - 1:
                while dq[0]["idx"] <= i - k:
                    dq.popleft()
                ans.append(dq[0]["val"])
        return ans
            



