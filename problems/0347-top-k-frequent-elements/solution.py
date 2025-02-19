class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        sortedArr = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            sortedArr[c].append(n)
    
        ans = []
        print(sortedArr)
        for i in range(len(sortedArr) - 1, -1, -1):
            vals = sortedArr[i]
            for n in vals:
                ans.append(n)
                if len(ans) == k:
                    return ans
        


