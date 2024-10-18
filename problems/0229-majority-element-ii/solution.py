class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums) // 3
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        ans = []
        for n, c in count.items():
            if c > k:
                ans.append(n)
        
        return ans
