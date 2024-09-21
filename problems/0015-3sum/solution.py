class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break # no 3 pos will sum to zero
            
            if i > 0 and nums[i - 1] == nums[i]:
                continue # avoid duplicate solutions
            
            l = i + 1
            r = len(nums) - 1

            while l < r:

                sum = nums[i] + nums[l] + nums[r]

                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l > 0 and l < r and nums[l] == nums[l - 1]:
                        l += 1 # avoid duplicate solutions
        return ans
                




