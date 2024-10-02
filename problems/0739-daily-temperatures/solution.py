class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        for i, t in enumerate(temperatures):
            temps.append({"temp": t, "idx": i})
        
        days = [0] * len(temps)

        # add temp to stack, while temp is higher than the top of the stack pop and assign the diff in idx to the days array

        stack = []
        for currDay in temps:
            
            while stack and stack[-1]["temp"] < currDay["temp"]:
                dayCount = currDay["idx"] - stack[-1]["idx"]
                priorDayIdx = stack[-1]["idx"]
                days[priorDayIdx] = dayCount
                stack.pop()
            
            stack.append(currDay)
        
        return days
