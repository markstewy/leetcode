class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxVolume = 0;
        int l = 0;
        int r = height.size() - 1;
        while (l < r) {
            int h = std::min(height[l], height[r]);
            int w = r - l;
            maxVolume = std::max(maxVolume, w * h);
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return maxVolume;
    }
};