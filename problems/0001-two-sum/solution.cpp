class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        // key = num and value = index
        unordered_map<int, int> cache;

        int i = 0;
        for (int n : nums) {
            int diff = target - n;

            if (cache.find(diff) != cache.end()) {
                return {i, cache[diff]};
            }

            cache[n] = i;

            i++;
        }
        // no answer found
        return {-1, -1};
    }
};
