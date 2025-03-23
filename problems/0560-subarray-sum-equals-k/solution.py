class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totals = []
        total = 0
        for n in nums:
            total += n
            totals.append(total)

        totalsIdx = collections.defaultdict(list)
        for i, t in enumerate(totals):
            totalsIdx[t].append(i)
        
        count = 0
        for i, t in enumerate(totals):
            diff = t - k
            if diff == 0:
                count += 1
            if diff in totalsIdx:
                for idx in totalsIdx[diff]:
                    if idx < i:
                        count += 1
        
        return count
