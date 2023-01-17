#include<set>
// solution reached in under 3 minutes
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> uniqueNums;
        for (int n : nums) {
            uniqueNums.insert(n);
        }
        return nums.size() != uniqueNums.size();
    }
};

