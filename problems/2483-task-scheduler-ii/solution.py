class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        
        wait = {} # key: task val: next date task can be done

        day = 0
        for t in tasks:
            day += 1

            if t in wait:
                day = max(wait[t], day)

            wait[t] = day + space + 1
        
        return day
