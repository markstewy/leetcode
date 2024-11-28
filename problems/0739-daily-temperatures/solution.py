class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        stack = []

        for i, t in enumerate(temps):

            while stack and t > stack[-1]["temp"]:
                idx = stack[-1]["idx"]
                ans[idx] = i - idx
                stack.pop()
            
            stack.append({"temp": t, "idx": i})
        
        return ans
        

