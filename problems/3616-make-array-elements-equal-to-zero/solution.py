class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return len(nums) * 2

        ltr, rtl = [], []

        t = 0
        for n in nums:
            t += n
            ltr.append(t)
        
        t = 0
        for i in range(len(nums) - 1, -1, -1):
            t += nums[i]
            rtl.append(t)
        rtl.reverse()
    
        print(rtl)
        print(ltr)

        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                l = ltr[i - 1] if i > 0 else 0
                r = rtl[i + 1] if i < len(nums) - 1 else 0

                if l == r + 1 or r == l + 1:
                    ans += 1
                if l == r:
                    ans += 2
        
        return ans


            
