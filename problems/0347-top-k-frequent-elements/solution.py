class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        sortedFrequency = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            sortedFrequency[c].append(n)
        
        ans = []
        for i in range(len(sortedFrequency) - 1, -1, -1):
            kFrequentValues = sortedFrequency[i]
            for n in kFrequentValues:
                ans.append(n)
                if len(ans) == k:
                    return ans
        
        return []
