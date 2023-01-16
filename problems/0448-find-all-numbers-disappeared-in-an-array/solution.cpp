

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> temp(nums.size(), -1);
        for (int n : nums) {
            temp[n - 1] = n;
        }
        vector<int> solution;
        for (int i = 0; i < temp.size(); i++) {
           if (temp[i] < 0) {
               solution.push_back(i + 1);
           } 
        }
        return solution;
    }
};
