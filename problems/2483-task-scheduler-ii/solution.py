class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        resumeDay = {}

        day = 0
        for t in tasks:
            if t in resumeDay:
                day = max(day, resumeDay[t])
            day += 1
            resumeDay[t] = day + space
    
        return day



