#include <unordered_map>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> m;
        
        for (int n : nums) {
            if (m[n] == 1) {
                return true;
            } else {
                m[n] = 1;
            }
        }
        return false;
    }
};
