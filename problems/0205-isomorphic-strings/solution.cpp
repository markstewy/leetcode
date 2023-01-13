#include <unordered_map>

class Solution {
public:
    
    bool checkOneWayTranslation (string a, string b) {
        unordered_map<char, char> m;
        
        // a dictionary for translating a to b
        for (int i = 0; i < a.size(); i++) {
            m[a[i]] = b[i];
        }
        
        string a_to_b_translation;
        for (char c : a) {
            a_to_b_translation.push_back(m[c]);
        }
        return a_to_b_translation == b;
    }
    
    bool isIsomorphic(string s, string t) {
        return checkOneWayTranslation(s, t) && checkOneWayTranslation(t, s);
    }
};
