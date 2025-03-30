class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        totals = []
        total = 0
        for n in nums:
            total += n
            totals.append(total)
        

        mods = collections.defaultdict(list)
        for i, t in enumerate(totals):
            mod = t % k

            if mod in mods and i - min(mods[mod]) >= 2:
                return True
            if mod == 0 and i > 0:
                return True

            mods[mod].append(i)

        return False
