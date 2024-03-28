class Solution:
    def trap(self, height: List[int]) -> int:
        ltr, rtl = [], []

        mh = 0
        for n in height:
            mh = max(mh, n)
            ltr.append(mh)

        mh = 0
        for i in range(len(height) - 1, -1, -1):
            mh = max(mh, height[i])
            rtl.append(mh)
        rtl.reverse()

        water = 0
        for i in range(1, len(height) - 1):
            w = min(ltr[i - 1], rtl[i + 1]) - height[i]
            if w > 0:
                water += w

        return water
