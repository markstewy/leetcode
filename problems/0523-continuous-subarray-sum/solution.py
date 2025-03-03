class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumRemainders = []
        total = 0
        for i, n in enumerate(nums):
            total += n
            
            if total % k == 0 and i > 0:
                return True
            
            sumRemainders.append(total % k)
        
        print(sumRemainders)
        remainderCount = collections.defaultdict(list) # remainder: [idx]

        for i, n in enumerate(sumRemainders):
            remainderCount[n].append(i)
        
        for idxs in remainderCount.values():
            if max(idxs) - min(idxs) > 1:
                return True
            
        return False

        
