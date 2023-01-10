class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s.size() == 0) {
            return true;
        }
        
        int i = -1;
        
        for (char c : s) {
            i++;
            while (i < t.size() && t[i] != c) {
                i++;
            }
        }

        return i < t.size();
    }
};
