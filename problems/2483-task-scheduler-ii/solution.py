class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 0
        wait = {}

        for t in tasks:
            day += 1
            if t in wait:
                day = max(day, wait[t])
            
            wait[t] = day + space + 1

        return day

