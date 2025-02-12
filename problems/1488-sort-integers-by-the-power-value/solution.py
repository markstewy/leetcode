class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        stepCounts = []
        cache = {} # n: stepCount
        
        for i in range(lo, hi + 1):
            n = i
            stepCount = 0
            
            while True:
                if n in cache:
                    stepCount = cache[n]
                    n = 1
                if n == 1:
                    stepCounts.append([stepCount, i])
                    break
                if n % 2 == 0:
                    n /= 2
                else:
                    n = 3 * n + 1
                
                stepCount += 1
        
        stepCounts.sort()

        return stepCounts[k-1][1]

