class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        wait = {}

        day = 0
        for t in tasks:
            if t in wait and wait[t] > day:
                day = wait[t]
            else:
                day += 1
            
            wait[t] = day + space + 1
        
        return day
            
