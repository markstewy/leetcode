class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
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
            if i == 0:
                ans.append(rtl[1])
            elif i == len(nums) - 1:
                ans.append(ltr[-2])
            else:
                ans.append(ltr[i - 1] * rtl[i + 1])
        return ans
