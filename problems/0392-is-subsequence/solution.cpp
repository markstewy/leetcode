// solution in 7 minutes
class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s == t) return true;
        
        int idxS = 0;
        int idxT = 0;
        
        while (idxT < t.size()) {
            if (s[idxS] == t[idxT]) {
                idxS++;
            }
            idxT++;
            
            if (idxS >= s.size()) {
                return true;
            }
        }
        return false;   
    }
};
