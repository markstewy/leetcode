class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sumIdxs = collections.defaultdict(list)
        maxSum = -1
        
        for n in nums:
            digits = [int(n) for n in list(str(n))]
            total = sum(digits)
            heapq.heappush(sumIdxs[total], -n)
        
        for hp in sumIdxs.values():
            if len(hp) > 1:
                total = -heapq.heappop(hp) + -heapq.heappop(hp)
                maxSum = max(maxSum, total)
        
        return maxSum
        


            
            
