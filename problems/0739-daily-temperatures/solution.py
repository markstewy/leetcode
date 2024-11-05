class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        stack = [] # {"idx":, "temp":}

        for i, t in enumerate(temps):
            while stack and stack[-1]["temp"] < t:
                days = i - stack[-1]["idx"]
                ans[stack[-1]["idx"]] = days
                stack.pop()
            
            stack.append({"idx": i, "temp": t})
        
        return ans
