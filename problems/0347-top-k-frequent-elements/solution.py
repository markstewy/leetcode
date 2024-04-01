class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        sorted_n_time_arrays = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            sorted_n_time_arrays[c].append(n)
        
        for i in range(len(sorted_n_time_arrays) - 1, -1 , -1):
            for n in sorted_n_time_arrays[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        
        return []
