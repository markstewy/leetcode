class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        totals = []
        total = 0
        for n in nums:
            total += n
            totals.append(total)
        
        mods = []
        for t in totals:
            mods.append(t % k)
        
        modMap = collections.defaultdict(list)

        for i, m in enumerate(mods):
            modMap[m].append(i)
        
        for i, m in enumerate(mods):
            if m == 0 and i > 0:
                return True
            
            if i - min(modMap[m]) > 1:
                return True
        
        return False


