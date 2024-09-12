class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr, rtl = [], []

        sum = 1
        for n in nums:
            sum *= n
            ltr.append(sum)
        
        sum = 1
        for i in range(len(nums) - 1, -1, -1):
            sum *= nums[i]
            rtl.append(sum)
        rtl.reverse()

        solution = []

        for i in range(len(nums)):
            if i == 0:
                solution.append(rtl[i + 1])
            elif i == len(nums) - 1:
                solution.append(ltr[i - 1])
            else:
                solution.append(ltr[i - 1] * rtl[i + 1])
        
        return solution

