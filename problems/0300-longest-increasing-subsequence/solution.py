class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        def closestNext(arr, target, closestNextIdx = 0):
            l = 0
            r = len(arr) - 1
            while l <= r:
                m = l + (r - l) // 2
                if arr[m] >= target:
                    closestNextIdx = m
                    r = m - 1
                else:
                    l = m + 1
            return closestNextIdx

        for n in nums:
            if n > dp[-1]:
                dp.append(n)
            else:
                insertIdx = closestNext(dp, n)
                dp[insertIdx] = n
        
        return len(dp)
