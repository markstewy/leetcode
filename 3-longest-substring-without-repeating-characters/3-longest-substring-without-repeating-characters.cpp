#include <unordered_map>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() == 0 || s.length() == 1) {
            return s.length();
        }
        std::unordered_map<char, int> x;
        int size = 0;
        int maxSize = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (x.find(s[i]) == x.end()) {
                x[s[i]] = i;
                size++;
                maxSize = std::max(size, maxSize); 
            } else {
                i = x[s[i]];
                size = 0;
                x.clear();
            }
        }
        return maxSize;
    }
};