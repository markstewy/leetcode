class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # n -> count
        ans = []

        for n in nums:
            count[n] = count.get(n, 0) + 1

        
        order = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            order[c].append(n)
        

        for i in range(len(order) - 1, -1, -1):
            for n in order[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
