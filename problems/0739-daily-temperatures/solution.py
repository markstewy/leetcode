class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            
            while stack and t > stack[-1]["temp"]:
                topIdx = stack[-1]["idx"]
                ans[topIdx] = i - topIdx
                stack.pop()

            stack.append({"temp": t, "idx": i})
        
        return ans
