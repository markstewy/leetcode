class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        sortedByCount = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            sortedByCount[c].append(n)
        

        ans = []
        for i in range(len(sortedByCount) - 1, -1, -1):
            vals = sortedByCount[i]
            for v in vals:
                ans.append(v)
                if len(ans) == k:
                    return ans
        
        return ans
