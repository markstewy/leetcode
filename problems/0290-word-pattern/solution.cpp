class Solution {
// solution in 18 mintues
public:
    bool wordPattern(string pattern, string s) {
        vector<string> sv;
        string word = "";
        for (char c : s) {
            if (c == ' ') {
                if (word.size() > 0) sv.push_back(word);
                word = "";
            } else {
                word.push_back(c);
            }
        }
        sv.push_back(word);
        
        if (sv.size() != pattern.size()) return false;
        
        unordered_map<char, string> cs;
        unordered_map<string, char> sc;
        
        for (int i = 0; i < sv.size(); i++) {
            cs[pattern[i]] = sv[i];
            sc[sv[i]] = pattern[i];
        }
        
        string s_to_c = "";
        string c_to_s = "";
        for (int i = 0; i < sv.size(); i++) {
        s_to_c += sc[sv[i]];
        c_to_s += cs[pattern[i]];
        if (i < sv.size() - 1) c_to_s += " ";
        }
        
        return s_to_c == pattern && c_to_s == s;
        
    }
};
