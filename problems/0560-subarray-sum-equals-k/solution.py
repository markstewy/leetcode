class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        totals = []
        total = 0
        for n in nums:
            total += n
            totals.append(total)
        
        totalsMap = collections.defaultdict(list)
        for i, t in enumerate(totals):
            totalsMap[t].append(i)
        
        count = 0
        for i, t in enumerate(totals):
            if t == k:
                count += 1
                
            target = -(k - t)
            if target in totalsMap:
                for j in totalsMap[target]:
                    if j < i:
                        count += 1
        
        return count
        

        
