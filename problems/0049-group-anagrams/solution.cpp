#include<unordered_map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> sol;
        unordered_map<string, vector<string>> cache; // <aplph_name key, vector of original strings>

        for (string s : strs) {
            string temp = s;
            std::sort(s.begin(), s.end()); 
            
            if (cache.find(s) != cache.end()) {
                cache[s].push_back(temp);
            } else {
                cache[s] = {temp};
            }
        }

        for (auto p : cache) {
            sol.push_back(p.second);
        }

        return sol;


    }
};
