class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
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


        total = 0
        for i in range(1, len(height) - 1): # double check endof range in case it's not the right index, should be [-2]
            waterLevel = min(ltr[i - 1], rtl[i + 1])
            floor = height[i]
            vol = max(0, waterLevel - floor)
            total += vol
        
        return total
