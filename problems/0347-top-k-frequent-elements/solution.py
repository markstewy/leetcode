class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {} # n -> count
        ans = []

        for n in nums:
            cache[n] = cache.get(n, 0) + 1


        sortedArr = [[] for _ in range(len(nums) + 1)]
        for n, c in cache.items():
            sortedArr[c].append(n)
        
        for i in range(len(sortedArr) - 1, -1, -1):
            for n in sortedArr[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

