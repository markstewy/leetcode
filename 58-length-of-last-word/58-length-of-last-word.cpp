class Solution {
public:
    int lengthOfLastWord(string s) {
        int l = 0;
        bool wordFound = false;
        for (int i = s.length() - 1; i >= 0; i--) {
            char x = s[i];
            if (s[i] == ' ' && wordFound) {
                return l;
            }
            if (s[i] != ' ') {
                wordFound = true;
                l++;
            }
        }
        return l;
    }
};