class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # dq where the right collpases on any values less than and the left loses any values out of the window
        # the max wil always be in position[0] ie. dq[0]

        dq = deque()
        ans = []

        # add
        for i, n in enumerate(nums):
            while dq and dq[-1]["val"] <= n:
                dq.pop()
            dq.append({"idx": i, "val": n})

            while dq and dq[0]["idx"] <= i - k:
                dq.popleft()
        
            kFirstIdx = k - 1
            if i >= kFirstIdx:
                ans.append(dq[0]["val"])
        
        return ans




        # start recroding max only after you get to window size
