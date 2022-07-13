#include <algorithm>
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> merged;
        //edge cases
        if (nums1.size() == 0) {
            merged = nums2;
        } else if (nums2.size() == 0) {
            merged = nums1;
        } else if (nums1.size() == 0 && nums2.size() == 0) {
            return 0.0;
        } else {
            std::merge(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), std::back_inserter(merged));    
        }
        
        if (merged.size() % 2 == 0) {
            int centerLeft = (merged.size() / 2) - 1;
            int centerRight = centerLeft + 1;
            
            double centerLeftValue = (double)merged[centerLeft];
            double centerRightValue = (double)merged[centerRight];
            return (centerLeftValue + centerRightValue) / 2.0;
        } else {
            int center = merged.size() / 2;
            return (double)merged[center];
        }
    }
};