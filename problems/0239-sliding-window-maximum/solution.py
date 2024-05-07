class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [] 
        dq = collections.deque()
        # [6]

        l = 0
        for r in range(len(nums)):
            # add to deque, if higher pop right first
            while len(dq) > 0 and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)

            if r >= k - 1:
                # the index in dq[0] should be the max for that window
                ans.append(nums[dq[0]])

                # if left position (idx) in deque is == l then pop left
                if dq[0] == l:
                    dq.popleft()
                l += 1
        
        return ans
