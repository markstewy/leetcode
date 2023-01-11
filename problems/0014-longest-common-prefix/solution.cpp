#include <algorithm>

auto sortBySize = [](std::string a, std::string b) {
    return a.size() < b.size();
};

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        std::sort(strs.begin(), strs.end(), sortBySize);
        
        if (strs.size() == 1) {
            return strs[0];
        }
        
        if (strs.size() == 0) {
            return "";
        }
        
        std::string cp = "";
        
        for (int col = 0; col < strs[0].size(); col++) {
            char c = strs[0][col];
            for (int row = 1; row < strs.size(); row++) {
                if (strs[row][col] != c) {
                    return cp;
                }
            }
            cp += c;
        }
        return cp;
    }
};
