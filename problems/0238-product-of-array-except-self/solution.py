class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr, rtl = [], []
        
        prod = 1
        for n in nums:
            prod = n * prod
            ltr.append(prod)

        nums.reverse()
        prod = 1
        for n in nums:
            prod = n * prod
            rtl.append(prod)
        rtl.reverse()          

        answer = []
        for i in range(0, len(nums)):
            print(i)
            l, r = 1, 1
            if i > 0:
                l = ltr[i - 1]
            if i < (len(nums) - 1):
                r = rtl[i + 1]
            answer.append(l * r)
        
        return answer
