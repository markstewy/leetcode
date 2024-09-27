class Solution:
    def trap(self, height: List[int]) -> int:
        ltr, rtl = [], []
        total = 0

        mh = 0
        for h in height:
            mh = max(h, mh)
            ltr.append(mh)

        mh = 0
        for i in range(len(height) - 1, -1, -1):
            mh = max(mh, height[i])
            rtl.append(mh)
        rtl.reverse()
    
        for i in range(1, len(height) - 1): # don't include first and last idxs
            waterLvl = min(ltr[i - 1], rtl[i + 1])
            floor = height[i]
            vol = max(0, waterLvl - floor)
            total += vol

        return total

