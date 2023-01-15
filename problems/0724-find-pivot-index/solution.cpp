class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        vector<int> sums;
        int sum = 0;
        
        for (int n : nums) {
            sum += n;
            sums.push_back(sum);
        }
        
        int total = sums[sums.size() - 1];
        for (int i = 0; i < sums.size(); i++) {
            int leftSum = i == 0 ? 0 : sums[i - 1];
            int rightSum = total - sums[i];
            
            if (leftSum == rightSum) {
                return i;
            }
        }
        return -1;
    }
};
