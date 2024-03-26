class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #n -> c

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        sorted = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            sorted[c].append(n)
        
        ans = []
        for i in range(len(sorted) - 1, -1, -1):
            for n in sorted[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        
