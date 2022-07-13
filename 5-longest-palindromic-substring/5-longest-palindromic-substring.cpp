class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() <= 1) { return s; }
        if (s.size() == 2) { 
            if (s[0] == s[1]) { 
                return s; 
            } else {
                return s.substr(0, 1);
            }   
        }
        
        string longest = s.substr(0, 1);
        
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == s[i + 1]) { 
                string temp = getPal(s, i, i + 1); 
                if (temp.size() > longest.size()) { longest = temp; }
            }
            if (i > 0 && s[i - 1] == s[i + 1]) { 
                string temp = getPal(s, i - 1, i + 1); 
                if (temp.size() > longest.size()) { longest = temp; }
            }
        }
        return longest;
    }

    string getPal(string& s, int l, int r) {
        while (l > 0 
            && r < s.size()
            && s[l - 1] == s[r + 1]
              ) {
            l--;
            r++;
        }
        return s.substr(l, r - l + 1);
    }
};