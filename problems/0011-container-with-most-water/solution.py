class Solution:
    def maxArea(self, height: List[int]) -> int:
        ltr, rtl = [], []

        mh = 0
        for h in height:
            mh = max(mh, h)
            ltr.append(mh)
        
        mh = 0
        for i in range(len(height) - 1, -1, -1):
            mh = max(mh, height[i])
            rtl.append(mh)
        rtl.reverse()
    
        maxVol = 0
        l = 0
        r = len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            w = r - l

            maxVol = max(maxVol, w * h)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxVol


