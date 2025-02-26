class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_pre_sum = 0
        max_pre_sum = 0
        curr_sum = 0
        max_abs_sum = 0

        for n in nums:
            curr_sum += n
            max_abs_sum = max(max_abs_sum, abs(curr_sum - max_pre_sum), abs(curr_sum - min_pre_sum))
            max_pre_sum = max(max_pre_sum, curr_sum)
            min_pre_sum = min(min_pre_sum, curr_sum)
    
        return max_abs_sum

            
