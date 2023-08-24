#include <unordered_map>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m; // <n, count>
        vector<vector<int>> v(nums.size() + 1);

        for (int i = 0; i < nums.size(); i++) {
            if (m.find(nums[i]) == m.end()) {
                m.insert(std::make_pair(nums[i], 1));
            } else {
                m[nums[i]]++;
            }
        }

        for (const auto& pair : m) {
            int count = pair.second;
            int num = pair.first;
            v[count].push_back(num);
        }

        vector<int> sol;
        for (int outerEnd = v.size() - 1; outerEnd >= 0; outerEnd--) {
            for (int innerEnd = v[outerEnd].size() - 1; innerEnd >= 0; innerEnd--) { 
                sol.push_back(v[outerEnd][innerEnd]);
                if (sol.size() >= k) { return sol; }
            }
        }

        return {};
    }
};
