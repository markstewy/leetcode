class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # n: count

        for n in nums:
            count[n] = count.get(n, 0) + 1

        sortedArr = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            sortedArr[c].append(num)

        solution = []
        for i in range(len(sortedArr) - 1, -1, -1):
            countIndex = sortedArr[i]
            for n in countIndex:
                solution.append(n)
                if len(solution) == k:
                    return solution

        return []
