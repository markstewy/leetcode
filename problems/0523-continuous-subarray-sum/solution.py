class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # [23, 2,  4,  6,  7]
        # [23, 25, 29, 35, 42]
        #  5.  1.   5


        # [23, 2  ,4,  6,  6]
        #. 23. 25  29  35, 41
        #  2.  4.  1.   0.  5
        remainderIdx = {}

        total = 0
        for i, n in enumerate(nums):
            total += n
            remainder = total % k

            if remainder == 0 and i >= 1:
                return True

            if remainder in remainderIdx and i - remainderIdx[remainder] > 1 and i > 0:
                return True
            elif remainder not in remainderIdx:
                remainderIdx[remainder] = i
        
        return False
