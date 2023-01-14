#include <algorithm>
#include <unordered_map>

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> nums2Idx;
        for (int i = nums2.size() - 1; i >= 0; i--) {
            nums2Idx[nums2[i]] = i;
        }
        
        auto getNextGreater = [nums2](int current) {
            int next = current;

            while(next < nums2.size()) {
                if (nums2[next] > nums2[current]) return nums2[next];
                next++;
            }
            return -1;
        };
        
        vector<int> ans;
        for (int n : nums1) {
            ans.push_back(getNextGreater(nums2Idx[n]));
        }
        return ans;
    }
};
