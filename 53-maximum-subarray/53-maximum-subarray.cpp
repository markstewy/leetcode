#include <algorithm>
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int finalMax = INT_MIN;
        int tempMax = 0;

        for (int i = 0; i < nums.size(); i++) {
            tempMax += nums[i];
            finalMax = std::max(finalMax, tempMax);

            if (tempMax < 0) {
                tempMax = 0;
            } 
        }

        return finalMax;
    }
};

// if your trailing sum ever drops below zero it's a net loss....
// abandon the entire preceeding section and reset tempMax to zero (which is
// the same as setting it equal to the next index - basically resetting your subarray
// starting point to cutout the prior net losses)