class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiff = float("infinity")
        ans = 0
        
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                
                diff = abs(target - sum)
                if diff < minDiff:
                    minDiff = diff
                    ans = sum
                
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    return target
        return ans
                    
                    
                    
                    
                    
                    
                    
                    
                    
