class Solution:
    def minSwaps(self, data: List[int]) -> int:
        windowLen = data.count(1)
        maxWindowCount = 0
        windowCount = 0

        l = 0
        for r in range(len(data)):
            if data[r] == 1:
                windowCount += 1
            if r - l + 1 > windowLen:
                if data[l] == 1:
                    windowCount -= 1
                l += 1
            maxWindowCount = max(maxWindowCount, windowCount)
        
        return windowLen - maxWindowCount
