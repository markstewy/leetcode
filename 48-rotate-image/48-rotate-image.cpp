class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        vector<vector<int>> solution;
        
        for (int col = 0; col < matrix[0].size(); col++) {
            vector<int> current;
            for (int row = matrix.size() - 1; row >= 0; row--) {
                int t = matrix[row][col];
                current.push_back(matrix[row][col]); 
            }
            solution.push_back(current);
        }
        
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                matrix[i][j] = solution[i][j];    
            }
        }
    }
};