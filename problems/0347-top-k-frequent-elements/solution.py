class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)

        freq = [[] for _ in range(max(numCount.values()) + 1)]

        for n, c in numCount.items():
            freq[c].append(n)
        print(freq)
        ans = []
        for i in range(len(freq) - 1, -1, -1):
            nums = freq[i]
            for n in nums:
                ans.append(n)
                if len(ans) == k:
                    return ans
        
        return ans


