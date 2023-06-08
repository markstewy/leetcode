#include <unordered_map>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> cache;

        for (int n : nums) {
            if (cache.find(n) != cache.end()) {
                return true;
            } else {
                cache[n] = 1;
            }
        }
        return false;
    }
};
