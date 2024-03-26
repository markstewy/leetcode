class Solution:
    def trap(self, height: List[int]) -> int:
        ltrMax, rtlMax = [], []

        tallest = 0
        for n in height:
            tallest = max(n, tallest)
            ltrMax.append(tallest)

        tallest = 0
        for i in range(len(height) - 1, -1, -1):
            tallest = max(tallest, height[i])
            rtlMax.append(tallest)
        rtlMax.reverse()

        count = 0

        for i in range(1, len(height) - 1, 1):
            depth = min(ltrMax[i - 1], rtlMax[i + 1]) - height[i]
            if depth > 0:
                count += depth
        
        return count
            
