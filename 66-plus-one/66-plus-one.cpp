class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size() - 1; i >= 0; i--) {
            digits[i] += 1;
            if(digits[i] > 9) {
                digits[i] = 0;
                if (i == 0) {
                    digits.insert(digits.begin(), 1);
                }
            } else {
                return digits;
            }
        }
        return digits;
    }
};