class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        stack = []

        for i , t in enumerate(temps):
            while stack and stack[-1]["temp"] < t:
                ans[stack[-1]["idx"]] = i - stack[-1]["idx"]
                stack.pop()

            stack.append({"temp": t, "idx": i})
        
        return ans

