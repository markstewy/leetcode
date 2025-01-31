class Solution:
    def minSwaps(self, data: List[int]) -> int:
        windowSize = sum(data)
        maxCount = 0
        count = 0
        
        l = 0
        for r in range(len(data)):
            if r - l + 1 > windowSize:
                count -= data[l]
                l += 1
            
            count += data[r]
            maxCount = max(maxCount, count)
        
        return windowSize - maxCount
            
                

