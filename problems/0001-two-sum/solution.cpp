#include <unordered_map>
// solution in 22 minutes
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, vector<int>> m; // <val, idxs>
        for (int i = 0; i < nums.size(); i++) {
           if (m.find(nums[i]) == m.end()) {
               m[nums[i]] = vector<int>{i};
           } else {
               m[nums[i]].push_back(i);
           }
        }
        
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            
            if (m.find(diff) != m.end()) {
                // can't add to itself unless 2 instances exist
                if (diff == nums[i] && m[diff].size() < 2) {
                    continue;
                }
                return {i, m[diff].back()};
            }
        }
        return {-1, -1};
    }
};
