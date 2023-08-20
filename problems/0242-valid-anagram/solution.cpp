#include<unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> sMap;
        unordered_map<char, int> tMap;

        for (int i = 0; i < s.size(); i++) {
            if (sMap.find(s[i]) == sMap.end()) {
                sMap.insert(std::make_pair(s[i], 1));
            } else {
                sMap[s[i]]++;
            }

            if (tMap.find(t[i]) == tMap.end()) {
                tMap.insert(std::make_pair(t[i], 1));
            } else {
                tMap[t[i]]++;
            }
        }

        for (auto& pair : sMap) {
            char sKey = pair.first;
            int sCount = pair.second;

            bool both_have_key = (tMap.find(sKey) != tMap.end());
            bool same_count = sCount == tMap[sKey];

            if (!both_have_key || !same_count) {
                return false;
            }
        }

        return true;
    }
};
