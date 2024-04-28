class Solution:
    def trap(self, height: List[int]) -> int:
        ltr, rtl = [], []
        tw = 0

        m = 0
        for n in height:
            m = max(m, n)
            ltr.append(m)
        

        m = 0
        for i in range(len(height) - 1, -1, -1):
            m = max(m, height[i])
            rtl.append(m)
        rtl.reverse()

        i = 1
        while i < len(height) - 1:
            l = ltr[i - 1]
            r = rtl[i + 1]
            top = min(l, r)
            bottom = height[i]

            depth = max(0, top - bottom)
            tw += depth

            i += 1

        return tw
