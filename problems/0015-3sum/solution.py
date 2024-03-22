class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i, n in enumerate(nums):
            #skip duplicate values
            if i > 0 and n == nums[i - 1]:
                continue
            #stop once you reach zeros, not possible to sum 3 positives to a zero value
            if n > 0:
                break

            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = n + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    ans.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                    while nums[r] < len(nums) - 1 and nums[r] == nums[r+1] and l<r:
                        r -= 1
        return ans
