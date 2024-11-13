class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        ans = []

        for i, n in enumerate(nums):
            while stack and stack[-1]["val"] < n:
                stack.pop()
            
            stack.append({"val": n, "idx": i})
        
            lastValidIdxInWindow = i - k + 1

            while stack and stack[0]["idx"] < lastValidIdxInWindow:
                stack.popleft()
            
            if lastValidIdxInWindow >= 0:
                ans.append(stack[0]["val"])
        
        return ans
