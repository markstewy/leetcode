class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        totals = []
        total = 0

        for n in nums:
            total += n
            totals.append(total)

        mods = [t % k for t in totals]
        print(totals)
        print(mods)

        # if the mod is 0 and not the first number
        # if two mods are the same the sum of the array beween those idxs is divisible by k
        modIdx = collections.defaultdict(list)

        for i, m in enumerate(mods):
            if m == 0 and i > 0:
                return True
        
            modIdx[m].append(i)
            if max(modIdx[m]) - min(modIdx[m]) > 1:
                return True
        
        return False
