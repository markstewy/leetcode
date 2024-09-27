class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # n: count

        for n in nums:
            count[n] = count.get(n, 0) + 1
        

        sArr = [[] for _ in range(len(nums) + 1)]
    
        for n, c in count.items():
            sArr[c].append(n)
        
        ans = []
        for i in range(len(sArr) - 1, -1, -1):
            values = sArr[i]
            for v in values:
                ans.append(v)
                if len(ans) == k:
                    return ans
        
        return []
