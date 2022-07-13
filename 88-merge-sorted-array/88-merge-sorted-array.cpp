class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if (m == 0) { nums1 = nums2; return; }
        if (n == 0) { return; }
        
        vector<int> temp;
        int i1 = 0;
        int i2 = 0;
        
        while (i1 < m || i2 < n) {
            if (i1 >= m) {
                temp.push_back(nums2[i2]);
                i2++;
                continue;
            }
            if (i2 >= n) {
                temp.push_back(nums1[i1]);
                i1++;
                continue;
            }
            
            if (nums1[i1] < nums2[i2]) {
                temp.push_back(nums1[i1]);
                i1++;
            } else {
                temp.push_back(nums2[i2]);
                i2++;
            }
        }
        nums1 = temp;
    }
};