class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // create an unordered map to store arrays of strings by sorted key
        unordered_map<string, vector<string>>m;
        for (string s : strs) {
            string key = s;
            std::sort(key.begin(), key.end());
            
            if (m.find(key) == m.end()) {
                m[key] = {};
            }
            m[key].push_back(s);
        }

// loop over the map and convert it into an array
        vector<vector<string>> solution;
        for (auto& pair : m) {
            solution.push_back(pair.second);
        }

        return solution;
    }
};
