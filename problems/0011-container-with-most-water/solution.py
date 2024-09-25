class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        mvol = 0

        while l < r:
            h = min(height[l], height[r])
            vol = h * (r - l)
            mvol = max(mvol, vol)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return mvol
