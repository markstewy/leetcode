class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if abs(total - target) < abs(ans - target):
                    ans = total
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    break
        
        return ans
        # 0 1 1 1
