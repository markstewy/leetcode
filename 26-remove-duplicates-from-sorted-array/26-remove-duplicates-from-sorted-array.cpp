class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int c = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > nums[c]) {
                c++;
                nums[c] = nums[i];
            }
        }
        return c + 1;
    }
};