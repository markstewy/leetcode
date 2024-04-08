class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # n -> c
        ans = []

        for n in nums:
            count[n] = count.get(n, 0) + 1

        sortedArr = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            sortedArr[c].append(n)
        
        for i in range(len(sortedArr) - 1, -1, -1):
            for n in sortedArr[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
