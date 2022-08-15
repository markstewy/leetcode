#include <cmath>

class Solution {
public:
    Solution() {
        for (int i = 0; i < 31; i++) {
            powers.push_back(pow(2, i));
        }   
        for (auto x : powers) {
            cout << x << "\n";
        }
    }

    bool isPowerOfTwo(int n) {
        return (std::find(powers.begin(), powers.end(), n) != powers.end());  
    }
                             
private:
    vector<int> powers;
};
