#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> solution{0, 0};
        std::unordered_map<int, std::vector<int>> numsMap{};
        for (int i = nums.size() - 1; i >= 0; i--) {
            int value = nums[i];
            int index = i;
            // set the value as the key and the index as the value
            numsMap[value].push_back(index);
        }
         
        for (int i = 0; i <= nums.size(); i++) {
            int diff = target - nums[i];
            // check value exists as a key and that the vector isn't empty
            if (numsMap.find(diff) != numsMap.end() && !numsMap[diff].empty()) {
                // make sure we aren't adding same index to itself
                if (numsMap[diff][0] != i) {
                    solution[0] = i;
                    solution[1] = numsMap[diff][0];
                    break;
                    // if the first index listed under a key is the same as current,
                    // check if there is another index in the vector
                } else if (numsMap[diff].size() > 1) {
                    solution[0] = i;
                    solution[1] = numsMap[diff][1];
                    break;
                }
            }
        }
        return solution;
    }
};
