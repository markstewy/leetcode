class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        freqArr = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            freqArr[c].append(n)
        
        ans = []
        for i in range(len(freqArr) - 1 , -1 , -1):
            values = freqArr[i]
            for v in values:
                ans.append(v)
                if len(ans) == k:
                    return ans
        
        return []
