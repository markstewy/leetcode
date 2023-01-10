#include <unordered_map>
#include <algorithm>


class Solution {
public:

    
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, vector<int>> m;
        
        for (int i = 0; i < nums.size(); i++) {
            int n = nums[i];
                
            if (m.find(n) != m.end()) {
                m[n].push_back(i);
            } else {
                m[n] = std::vector<int>{i};
            }
        }
        
        for (int n : nums) {
            int diff = target - n;
            
            if (n == diff) {
                if (m[n].size() > 1) {
                    return std::vector<int>{m[n][0], m[n][1]};
                }
            } else {
                if (m[diff].size() > 0) {
                    return std::vector<int>{m[n][0], m[diff][0]};
                } 
            }
        }
        return std::vector<int>{-1, -1};
    }
};
