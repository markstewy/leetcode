class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) { return s; }
        
        
        vector<string> rows;
        string solution;
        for (int i = 0; i < numRows; i++) {
            rows.push_back("");
        }
        
        int curChar = 0;
        int row = 0;
        int increment = 1;
        
        while (curChar < s.size()) {
            rows[row] += s[curChar];
            curChar++;
            if (row == numRows - 1) { increment = -1; }
            if (row == 0) { increment = 1; }
            row += increment;
        }
        
        for (int i = 0; i < numRows; i++) {
            solution += rows[i];
        }
        return solution;
    }
};
