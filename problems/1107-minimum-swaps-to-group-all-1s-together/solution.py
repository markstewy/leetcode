class Solution:
    def minSwaps(self, data: List[int]) -> int:
        winSize = data.count(1)
        maxOnes = 0
        
        oneCount = 0
        l = 0
        for r in range(len(data)):
            if data[r] == 1:
                oneCount += 1

            if r - l + 1 > winSize:
                if data[l] == 1:
                    oneCount -= 1
                l += 1
            
            maxOnes = max(maxOnes, oneCount)
            
        return winSize - maxOnes
            
