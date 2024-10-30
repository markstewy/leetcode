class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        stack = [] # [{idx, temp}]

        for i, t in enumerate(temps):
            while stack and t > stack[-1]["temp"]:
                priorDay = stack[-1]["day"]
                ans[priorDay] = i - priorDay
                stack.pop()
            
            stack.append({"day": i, "temp": t})
        
        return ans

