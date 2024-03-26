class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, n in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            if n > 0:
                break # no 3 positive numbers will ever sum to zero

            if i > 0 and n == nums[i - 1]:
                continue # don't let i index repeat itself

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
                    while nums[l] == nums[l -1] and l < r:
                        l += 1 # don't let l index repeat itself
        return ans
