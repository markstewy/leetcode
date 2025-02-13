class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        count = 0
        while nums[0] < k:
            n1 = heapq.heappop(nums)
            n2 = heapq.heappop(nums)
            n3 = min(n1, n2) * 2 + max(n1, n2)
            heapq.heappush(nums, n3)
            count += 1
        
        return count
