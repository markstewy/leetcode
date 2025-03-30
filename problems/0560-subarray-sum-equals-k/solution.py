class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = collections.defaultdict(list) #sum: [idx]

        totals = []
        total = 0
        for i, n in enumerate(nums):
            total += n
            totals.append(total)
            prefixSums[total].append(i)
        

        count = 0
        for i, t in enumerate(totals):
            if t == k:
                count += 1

            diff = t - k

            if diff in prefixSums:
                for idx in prefixSums[diff]:
                    if idx < i:
                        count += 1
        
        return count

        

