class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        wait = {} # t: day

        day = 0
        for t in tasks:
            day += 1
            if t not in wait:
                wait[t] = day + space + 1
            else:
                day = max(day, wait[t])
                wait[t] = day + space + 1

        return day
