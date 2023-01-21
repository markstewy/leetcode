#include <unordered_map>
// solution in 5 minutes 
// O(n) worst case compated to 
// sorting alternative O(n logn)
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> m;
        int majority = (nums.size() / 2) + 1;
        
        for (int n : nums) {
            if (m.find(n) == m.end()) {
                m[n] = 1;
            } else {
                m[n] = m[n] + 1;
            }
            
            if (m[n] == majority) {
                return n;
            }
        }
        return -1;
    }
};
