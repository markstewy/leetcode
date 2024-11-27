class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        countArr = [[] for _ in range(len(nums) + 1)]

        for n, cnt in count.items():
            countArr[cnt].append(n)


        ans = []
        for i in range(len(countArr) - 1, -1, -1):
            values = countArr[i]
            for v in values:
                ans.append(v)
                if len(ans) == k:
                    return ans
        
        return []

    
