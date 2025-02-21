class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        stack = []

        for i, t in enumerate(temps):
            
            while stack and t > stack[-1][0]:
                priorIdx = stack[-1][1]
                days = i - priorIdx
                ans[priorIdx] = days
                stack.pop()
            
            stack.append([t, i])

        return ans

