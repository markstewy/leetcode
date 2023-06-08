class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> tally;

        for (int n : nums) {
            if (tally.find(n) != tally.end()) {
                tally[n] = tally[n] + 1;
            } else {
                tally[n] = 1;
            }
        }

        vector<vector<int>> v;
        for (auto p : tally) {
            int num = p.first;
            int count = p.second;
            v.push_back({num, count});
        }

        std::sort(v.begin(), v.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] > b[1];
        });

        vector<int> sol;

        for (int i = 0; i < k; i++) {
            sol.push_back(v[i][0]);
        }

        return sol;
    }
};
