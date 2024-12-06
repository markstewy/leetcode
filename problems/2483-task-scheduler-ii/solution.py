class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 0
        waitTimes = {}

        for t in tasks:
            day += 1

            if t in waitTimes:
                day = max(day, waitTimes[t])
            
            waitTimes[t] = day + space + 1
        
        return day
