class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> s; // <num, idx>

        int i = 0;
        for (int& n : nums) {

            int diff = target - n;
            if (s.find(diff) != s.end()) {
                return {s[diff], i};
            }

            s.insert(std::make_pair(n, i));
            i++;
        }

        return {-1, -1};
    }
};
