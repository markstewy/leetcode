#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> solution;
        // map all values <value: index>
        unordered_map<int, vector<int>> m;
        for (int i = 0; i < nums.size(); i++) {
            if (m.find(nums[i]) == m.end()) {
                pair<int, vector<int>>p;
                vector<int> temp{i};
                p.first = nums[i];
                p.second = temp;
                m.insert(p);
            } else {
                m[nums[i]].push_back(i);
            }
        }
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (m.find(diff) != m.end()) {
                for (int idx : m[diff]) {
                    if (idx != i) {
                        solution.push_back(i);
                        solution.push_back(idx);
                        return solution;
                    }
                }
            }
        }
        return solution;
    }

};