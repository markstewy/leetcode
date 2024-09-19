class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # {temp: number, idx: number}
        solution = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # if t is greater than prior, set idx differences in solution
            # else append to stack

            while stack and t > stack[-1]["temp"]:
                solution[stack[-1]["idx"]] = i - stack[-1]["idx"]
                stack.pop()
            
            stack.append({"temp": t, "idx": i})
        
        return solution
