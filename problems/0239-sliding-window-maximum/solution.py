class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # index
        ans = []
        l, r = 0 , 0

        while r < len(nums):
            # remove from right if smaller 
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove from left if out of window
            if l > q[0]:
                q.popleft()

            # add to ans if full window span
            if (r + 1) >= k:
                ans.append(nums[q[0]])
                l += 1
            r += 1
        
        return ans
