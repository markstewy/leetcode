class Solution {
public:
    bool validPalindrome(string s) {
        int l = 0;
        int r = s.length() - 1;
        
        while (l < r) {
            if (s[l] != s[r]) {
                string exeptionLeft = s.substr(l + 1, r - l);
                string exceptionRight = s.substr(l, r - l);
                return checkP(exeptionLeft) || checkP(exceptionRight);
            }
            r--;
            l++;
        }
        return true;
    }
    
    bool checkP(string s) {
        int l = 0;
        int r = s.length() - 1;
        
        while (l < r) {
            if (s[l] != s[r]) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};