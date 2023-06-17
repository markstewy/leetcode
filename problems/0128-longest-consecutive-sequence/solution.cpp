#include<algorithm>

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::sort(nums.begin(), nums.end(), [](int a, int b) { return a < b; });

        if (nums.size() <= 1) return nums.size();

        int longest = 1;
        int consec_length = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1]) continue;
            if (nums[i] == nums[i - 1] + 1) {
                consec_length++;
            } else {
                consec_length = 1;
            }
            if (consec_length > longest) {
                longest = consec_length;
            }
        }
        return longest;
    }
};
