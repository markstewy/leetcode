class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temps)

        for i, t in enumerate(temps):
            while stack and t > stack[-1]["temp"]:
                ans[stack[-1]["idx"]] = i - stack[-1]["idx"] # record number of days to get higher temp
                stack.pop()
            stack.append({"temp": t, "idx": i})
            
        
        return ans

        # BigO: O(n) linear time and space
