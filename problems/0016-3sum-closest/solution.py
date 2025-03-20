class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float("infinity")

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(target - total) < abs(target - closestSum):
                    closestSum = total

                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                elif total == target:
                    return total
        
        return closestSum

