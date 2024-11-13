class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        frequency = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            frequency[c].append(n)
        
        ans = []
        for i in range(len(frequency) - 1, -1, -1):
            values = frequency[i]
            for v in values:
                ans.append(v)
                if len(ans) == k:
                    return ans
