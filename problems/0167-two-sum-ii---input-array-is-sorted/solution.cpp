#include<unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, vector<int>> cache{}; // key: numVal, val: vector<idx>

        int i = 0;
        for (int num : numbers) {
            int diff = target - num;

            if (cache.find(diff) != cache.end()) {
                if (num == diff && cache[diff].size() >= 2) {
                    return {cache[diff][0] + 1, cache[diff][1] + 1}; // return 1st 2 idx from same key
                }
                return {cache[diff][0] + 1, i + 1}; // return idx and diff 1st idx
            }

            if (cache[num].size() == 0) {
                cache[num] = {i};
            } else {
                cache[num].push_back(i);
            }

            i++;
        }
        return {};
    }
};
