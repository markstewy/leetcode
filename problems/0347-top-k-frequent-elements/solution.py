class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # n -> c
        kArr = [[] for _ in range(len(nums) + 1)]
        ans = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            kArr[c].append(n)
        
        for i in range(len(kArr) - 1, -1, -1):
            for n in kArr[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

