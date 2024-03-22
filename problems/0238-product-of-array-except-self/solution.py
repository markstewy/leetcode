class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr, rtl = [], []

        p = 1
        for n in nums:
            p *= n
            ltr.append(p)

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            p *= nums[i]
            rtl.append(p)
        rtl.reverse()

        ans = []

        for i in range(len(nums)):
            l, r = 1, 1
            if i > 0:
                l = ltr[i - 1]
            if i < len(nums) - 1:
                r = rtl[i + 1]
            ans.append(l * r)
        return ans
