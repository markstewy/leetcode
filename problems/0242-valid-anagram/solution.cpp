#include <algorithm>



class Solution {
public:
    static constexpr auto sortBy = [] (char a, char b) {
        return a < b;
    };
    
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        
        std::sort(s.begin(), s.end(), Solution::sortBy);
        std::sort(t.begin(), t.end(), Solution::sortBy);
        
        return s == t;
    }
};
