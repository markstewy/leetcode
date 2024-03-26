class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr, rtl = [], []

        prod = 1
        for n in nums:
            prod *= n
            ltr.append(prod)
        
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            rtl.append(prod)
        rtl.reverse()

        ans = []

        for i in range(len(nums)):
            l = 1
            r = 1

            if i > 0:
                l = ltr[i - 1]
            if i < len(nums) - 1:
                r = rtl[i + 1]
            
            ans.append((l * r))
        return ans

