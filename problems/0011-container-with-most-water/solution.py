class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        mA = 0
        mhl = 0
        mhr = 0

        while l < r:
            mhl = max(mhl, height[l])
            mhr = max(mhr, height[r])
            mh = min(mhl, mhr)
            mA = max(mA, mh * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return mA
