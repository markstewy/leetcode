class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<std::string> solution;
        helper(solution, n, n, n, "");
        return solution;
    }
    
    void helper(vector<std::string>& solution, int n, int l, int r, std::string validCombo) {
        // base
        if (l == 0 && r == 0) {
            solution.push_back(validCombo);
        }
        
        // Add "}" right bracket
        if (r > 0 && r > l) { // there are enough left brackets to support an additional right bracket
            helper(solution, n, l, r - 1, validCombo + ")");
        }
        // Add "{" left bracket
        if (l > 0) {
            helper(solution, n, l - 1, r, validCombo + "(");
        }
    }
};