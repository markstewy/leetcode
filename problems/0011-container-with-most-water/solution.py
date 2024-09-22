class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        mVol = 0

        while l < r:
            vol = min(height[l], height[r]) * (r - l)
            mVol = max(mVol, vol)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return mVol
