class Solution {
public:
    bool isPalindrome(string s) {
        string valid = "qwertyuiopasdfghjklzxcvbnm1234567890";
        string clean_s;

        for (char c : s) {
            c = tolower(c);
            if (valid.find(c) != string::npos) {
                clean_s.push_back(c);
            }
        }

        if (clean_s.length() == 0) return true;

        int r = clean_s.length() - 1;
        for (int l = 0; l <= r; l++) {
            char lv = clean_s[l];
            char rv = clean_s[r];
            if (clean_s[l] != clean_s[r]) return false;
            r--;
        }
        return true;
    }
};
