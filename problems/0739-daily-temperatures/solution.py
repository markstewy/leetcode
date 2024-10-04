class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        days = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1]["temp"]:
                days[stack[-1]["idx"]] = i - stack[-1]["idx"]
                stack.pop()
            
            stack.append({"idx": i, "temp": t})
        
        return days
