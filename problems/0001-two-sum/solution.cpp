#include<unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> cache; // <num, index>

        int i = 0;
        for (int n : nums) {

            int diff = target - n;

            if (cache.find(diff) != cache.end()) {
                return {i, cache[diff]};
            } else {
                cache[n] = i;
            }
            i++;
        }

        return {-1, -1};
    }
};
