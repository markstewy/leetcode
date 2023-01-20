#include <unordered_map>

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) return false;
        
        unordered_map<char, char> tm;
        unordered_map<char, char> sm;
        for (int i = 0; i < s.size(); i++) {
            tm[s[i]] = t[i];
            sm[t[i]] = s[i];
        }
        
        string s_to_t, t_to_s;
        for (int i = 0; i < s.size(); i++) {
            s_to_t += tm[s[i]];
            t_to_s += sm[t[i]];
        }
        return s_to_t == t && t_to_s == s;
    }
};
