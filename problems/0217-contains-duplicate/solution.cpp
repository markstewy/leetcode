#include <unordered_map>
// solution in 2 minutes
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> m;
        
        for (int n : nums) {
            if (m.find(n) != m.end()) return true;
            m[n] = 1;
        }
        return false;
    }
};
