class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # array of the gap values
        gaps = []

        lastEnd = endTime[-1]
        
        if startTime[0] > 0:
            gaps.append(startTime[0])
        
        for i in range(1, len(startTime)):
            gaps.append(startTime[i] - endTime[i - 1])

        if endTime[-1] < eventTime:
            gaps.append(eventTime - endTime[-1])

        if not gaps:
            return 0
        
        window = k + 1
        maxGap = 0
        currGap = 0

        l = 0
        for r in range(len(gaps)):
            if r - l + 1 > window:
                currGap -= gaps[l]
                l += 1
            currGap += gaps[r]
            maxGap = max(currGap, maxGap)

        return maxGap
            
                
                
                

        # sliding window of size k get the max sum of gaps
        
