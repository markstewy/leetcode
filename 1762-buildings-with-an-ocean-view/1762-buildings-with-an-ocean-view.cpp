class Solution {
public:
    vector<int> findBuildings(vector<int>& heights) {
        int max = 0;
        vector<int> solution;
        vector<int> solutionSorted;
        for (int i = heights.size() - 1; i >= 0; i--) {
            if(heights[i] > max) {
                max = heights[i];
                solution.push_back(i);
            }
        }
        for (int i = solution.size() - 1; i >= 0; i--) {
            solutionSorted.push_back(solution[i]);   
        }
        return solutionSorted;
    }
};