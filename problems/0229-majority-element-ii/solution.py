class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        k = len(nums) / 3
        count = Counter(nums)
        
        for n, c in count.items():
            if c > k:
                ans.append(n)
        
        return ans
