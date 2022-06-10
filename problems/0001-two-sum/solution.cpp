#include <unordered_map>
#include <cmath>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) { // O 2n complexity (worst cast)
        // make a map {value, vector<int>}  
        vector<int> solution;
        unordered_map<int, vector<int>> numsMap;
        for (int i = 0; i < nums.size(); i++) {
            if (numsMap.find(nums[i]) == numsMap.end()) {
                vector<int> idxs{i};
                int val = nums[i];
                pair<int, vector<int>> p;
                p.first = val;
                p.second = idxs;
                numsMap.insert(p);
            }
        }
        // loop over array and check if the difference exists in the array
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            
            if (numsMap.find(diff) != numsMap.end()) {
                vector<int>& idxs = numsMap[diff];
                for (int idx : idxs) {
                    // make sure it's not the same index
                    if (idx != i) {
                        solution.push_back(i);
                        solution.push_back(idx);
                        // make and return the 2 idxs in an array
                        return solution;
                    }
                }
            }
        }
        return solution; // return empty array if no solution
    }
    
    // vector<int> twoSum(vector<int>& nums, int target) {
//         vector<int> solution{0, 0};
//         std::unordered_map<int, std::vector<int>> numsMap{};
//         for (int i = nums.size() - 1; i >= 0; i--) {
//             int value = nums[i];
//             int index = i;
//             // set the value as the key and the index as the value
//             numsMap[value].push_back(index);
//         }
         
//         for (int i = 0; i <= nums.size(); i++) {
//             int diff = target - nums[i];
//             // check value exists as a key and that the vector isn't empty
//             if (numsMap.find(diff) != numsMap.end() && !numsMap[diff].empty()) {
//                 // make sure we aren't adding same index to itself
//                 if (numsMap[diff][0] != i) {
//                     solution[0] = i;
//                     solution[1] = numsMap[diff][0];
//                     break;
//                     // if the first index listed under a key is the same as current,
//                     // check if there is another index in the vector
//                 } else if (numsMap[diff].size() > 1) {
//                     solution[0] = i;
//                     solution[1] = numsMap[diff][1];
//                     break;
//                 }
//             }
//         }
//         return solution;
//     }
};
