class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #O(n*logn)
        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break # there will never be 3 pos ints that sum to zero

            if i > 0 and nums[i] == nums[i - 1]:
                continue # avoid duplicates

            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return ans

        


