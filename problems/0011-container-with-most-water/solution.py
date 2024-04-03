class Solution:
    def maxArea(self, height: List[int]) -> int:
        mVol = 0
        lMax = 0
        rMax = 0

        l = 0
        r = len(height) - 1
        while l < r:
            lMax = max(lMax, height[l])
            rMax = max(rMax, height[r])
            vol = (r - l) * min(lMax, rMax)
            mVol = max(mVol, vol)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return mVol
