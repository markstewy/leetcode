#include <unordered_map>

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> sVec;
        string word;
        
        for (char c : s) {
            if (c == ' '){
                sVec.push_back(word);
                word = "";
                continue;
            } else {
                word.push_back(c);
            }
        }
        sVec.push_back(word);
        
        if (sVec.size() != pattern.size()) {
            return false;
        }
        
        unordered_map<char, string> m;
        unordered_map<string, char> m2;
        
        for (int i = 0; i < min(s.size(), pattern.size()); i++) {
            m[pattern[i]] = sVec[i];
            m2[sVec[i]] = pattern[i];
        }
        for (int i = 0; i < pattern.size(); i++) {
            if (m[pattern[i]] != sVec[i] || m2[sVec[i]] != pattern[i]) {
                return false;
            }
        }
        return true;
    }
};
