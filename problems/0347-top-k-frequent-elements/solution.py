class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sortedArr = [[] for _ in range(len(nums) + 1)]

        for n, cnt in count.items():
            sortedArr[cnt].append(n)

        ans = []
        for i in range(len(sortedArr) - 1, -1, -1):
            for v in sortedArr[i]:
                ans.append(v)
                if len(ans) == k:
                    return ans

