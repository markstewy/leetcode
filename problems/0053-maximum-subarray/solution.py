class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current sum and max sum with the first element
        current_sum = max_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # For each element, decide whether to start a new subarray 
            # or extend the existing subarray
            current_sum = max(num, current_sum + num)
            
            # Update the maximum sum if current sum is larger
            max_sum = max(max_sum, current_sum)
        
        return max_sum




