class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) { return s; }
        
        vector<string> rows;
        for (int i = 0; i < numRows; i++) {
            rows.push_back("");
        }
        
        int i = 0;
        int row = 0;
        int rowIncr = 1;
        while(i < s.size()) {
            rows[row] += s[i];
            
            row += rowIncr;
            i++;
            if (row == numRows - 1) { rowIncr = -1;}
            if (row == 0) { rowIncr = 1;}
        }
        
        string solution = "";
        for (int i = 0; i < numRows; i++) {
            solution += rows[i];
        }
        return solution;
    }
};