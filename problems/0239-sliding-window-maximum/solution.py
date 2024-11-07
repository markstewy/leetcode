class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque() # {"idx": , "num":}
        ans = []

        for i, n in enumerate(nums):
            while stack and n > stack[-1]["num"]:
                stack.pop()
            
            stack.append({"idx": i, "num": n})
        
            lastIdxInWindow = i - k + 1

            while stack[0]["idx"] < lastIdxInWindow:
                stack.popleft()
            
            if lastIdxInWindow >= 0:
                ans.append(stack[0]["num"])
        
        return ans
