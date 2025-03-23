class Solution:
    def check(self, nums: List[int]) -> bool:
        decreaseCount = 0

        prev = nums[-1]
        for n in nums:
            if n < prev:
                decreaseCount += 1
            prev = n
        
        return decreaseCount <= 1
