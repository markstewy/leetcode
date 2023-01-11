class Solution {
public:
    void clearBack(vector<int>& nums, int val) {
        while(nums.size() > 0 && nums.back() == val) {
            nums.pop_back();
        }
    }
    
    int removeElement(vector<int>& nums, int val) {
        if (nums.size() == 0) {
            return 0;
        }
        if (nums.size() == 1 && nums[0] == val) {
            nums.pop_back();
            return 0;
        }
        
        
        clearBack(nums, val);
        
        int i = 0;
        while (i < nums.size() && nums.size() > 1) {
            if(nums[i] == val) {
                nums[i] = nums.back();
                nums.pop_back();
                clearBack(nums, val);   
            }
            i++;
        }
        return nums.size();
    }
};
