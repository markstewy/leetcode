class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {} # n: count

        for n in nums:
            cache[n] = cache.get(n, 0) + 1
        
        sortedArr = [[] for _ in range(len(nums) + 1)]

        for n, c in cache.items():
            sortedArr[c].append(n)
        

        solution = []
        for i in range(len(sortedArr) - 1, -1, -1):
            values = sortedArr[i]
            for n in values:
                solution.append(n)
                if len(solution) == k:
                    return solution

