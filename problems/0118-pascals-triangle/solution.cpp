class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        std::vector<std::vector<int>> solution{};
        if (numRows <= 0) { return solution; }
        solution.push_back(std::vector<int>{1});
        if (numRows == 1) { return solution; }
        solution.push_back(std::vector<int>{1, 1});
        if (numRows == 2) { return solution; }
        
        
        for (int i = 2; i < numRows; i++) {
            std::vector<int> prior = solution[i - 1];
            
            std::vector<int> temp{1};
            for (int j = 1; j < i; j++) {
                temp.push_back(prior[j] + prior[j - 1]);
            }
            temp.push_back(1);
            solution.push_back(temp);
        }
        return solution;
    }
};

