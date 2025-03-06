class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        totals = []
        total = 0
        mods = []
        for i, n in enumerate(nums):
            total += n
            mod = total % k
            
            if mod == 0 and i > 0:
                return True

            totals.append(total)
            mods.append(mod)
        
        print(totals)
        print(mods)
        modIdxs = collections.defaultdict(list)
        for i, n in enumerate(mods):
            modIdxs[n].append(i)
        
        for m, idxs in modIdxs.items():
            if max(idxs) - min(idxs) > 1:
                return True
        
        return False



