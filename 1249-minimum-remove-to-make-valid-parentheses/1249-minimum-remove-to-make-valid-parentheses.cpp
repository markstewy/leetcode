#include <cmath>

class Solution {
public:
    string minRemoveToMakeValid(string s) {   
        int balanced = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') balanced++;
            if (s[i] == ')') balanced--;
            if (balanced < 0) {
                s.erase(i, 1);
                i--;
                balanced++;
            }
        }
        balanced = 0;
        for (int i = s.size() - 1; i >= 0; i--) {
            if (s[i] == '(') balanced--;
            if (s[i] == ')') balanced++;
            if (balanced < 0) {
                s.erase(i, 1);
                balanced++;
            }
        }
        return s;
    }
};