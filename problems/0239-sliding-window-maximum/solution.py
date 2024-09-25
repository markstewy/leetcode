class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()
        ans = []

        for i, n in enumerate(nums):
            while dq and dq[-1]["val"] < n:
                dq.pop()
            dq.append({"val": n, "idx": i})

            if i >= k - 1:
                while dq and dq[0]["idx"] <= i - k:
                    dq.popleft()
            
                ans.append(dq[0]["val"])
        return ans  

