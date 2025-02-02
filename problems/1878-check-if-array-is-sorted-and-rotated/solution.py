class Solution:
    def check(self, nums: List[int]) -> bool:
        mn = min(nums)
        mnIdx = None

        for i in range(len(nums) - 1, -1, -1):
            if i == 0 or (nums[i] == mn and nums[i-1] > nums[i]):
                mnIdx = i
                break

        prev = -float("infinity")

        for i in range(len(nums)):
            idx = (i + mnIdx) % len(nums)
            if nums[idx] < prev:
                return False
            prev = nums[idx]
        
        return True
