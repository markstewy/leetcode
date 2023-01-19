// solution in 15 minutes
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        string pre = "";
        
        for (int i = 0; i < strs[0].size(); i++) {
            char c = strs[0][i];
            
            for (int s = 1; s < strs.size(); s++) {
                if (i >= strs[s].size() || strs[s][i] != c) return pre;
            }
            
            pre.push_back(c);
        }
        return pre;
    }
};
