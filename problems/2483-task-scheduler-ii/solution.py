class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        delay = {}
        day = 0

        for t in tasks:
            day += 1

            if t in delay and delay[t] >= day:
                    day = delay[t] + 1

            delay[t] = day + space
        
        return day
            

