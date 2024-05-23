class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # keep a list of max
        # if a newly added n is greater than nums to the left, remove the nums on the left
        # the max for a window will always be the n in position 0
        # remove the position 0 if it's index is no longer in the window

        # track index to make sure it's removed from the window
        # track val to knwo if it should overwrite values to the left
        # use a double sided queue so you can pop from the front or the back at constant time

        dq = collections.deque()
        ans = []

        l = 0
        for r, n in enumerate(nums):
            while len(dq) > 0 and dq[-1]["num"] < n:
                dq.pop()
            
            # add r index and val
            dq.append({"idx": r, "num": n})
            
            if (r - l + 1) >= k:
                while dq[0]["idx"] < l:
                    dq.popleft()
                
                ans.append(dq[0]["num"])
                l += 1
        
        return ans

        
