class Solution {
public:
    // solution in 17 minutes    
    vector<int> getNextRow(vector<int> prior) {
        vector<int> row{1};
        for (int i = 1; i < prior.size(); i++) {
            row.push_back(prior[i - 1] + prior[i]);
        }
        row.push_back(1);
        return row;
    }
    
    vector<vector<int>> generate(int numRows) {
        if (numRows == 0) return {};
        if (numRows == 1) return {{1}};
        if (numRows == 2) return {{1}, {1, 1}};
        
        vector<vector<int>> solution{{1}, {1, 1}};
        for (int r = 3; r <= numRows; r++) {
            vector<int> priorRow = solution.back();
            solution.push_back(getNextRow(priorRow));
        }
        return solution;
    }
};
