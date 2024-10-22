class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = [] # {temp, idx}
        ans = [0] * len(temps)

        for i, t in enumerate(temps):
            while stack and t > stack[-1]["temp"]:
                idx = stack[-1]["idx"]
                days = i - stack[-1]["idx"]
                ans[idx] = days
                stack.pop()

            stack.append({"temp": t, "idx": i})

        
        return ans
